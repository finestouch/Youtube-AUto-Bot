from __future__ import annotations

from app.ai.multi_agent import MultiAgentSignalEngine
from app.ai.regime_detector import MarketRegimeDetector
from app.ai.rl_engine import ReinforcementLearningDecisionEngine
from app.core.config import settings
from app.core.models import Action, EngineDecision
from app.data.collector import DataCollector
from app.execution.trade_executor import TradeExecutor
from app.features.engineering import FeatureEngineer
from app.risk.manager import RiskManager


class TradingOrchestrator:
    def __init__(self) -> None:
        self.collector = DataCollector()
        self.fe = FeatureEngineer()
        self.regime = MarketRegimeDetector()
        self.ma = MultiAgentSignalEngine()
        self.rl = ReinforcementLearningDecisionEngine()
        self.risk = RiskManager()
        self.executor = TradeExecutor()

    def run_cycle(self, symbol: str = "BTCUSDT", quantity: float = 0.1) -> dict:
        snapshot = self.collector.collect(symbol)
        features = self.fe.build(snapshot)
        regime = self.regime.classify(features)
        votes, liquidity_trap = self.ma.evaluate(features)
        positive_votes = sum(1 for v in votes if v.vote and v.agent != "liquidity_trap_agent")

        proposed = self.ma.infer_action(positive_votes, settings.min_votes_required)
        rl_action, confidence = self.rl.score_action(features, proposed)

        blocked = liquidity_trap and settings.block_on_liquidity_trap
        reasons = [v.reason for v in votes if v.vote]
        if blocked:
            rl_action = Action.HOLD
            reasons.append("liquidity trap detected")

        ok, risk_reason = self.risk.can_trade(rl_action, confidence)
        reasons.append(risk_reason)
        decision = EngineDecision(rl_action, confidence, regime, positive_votes, blocked, reasons)

        order = None
        if ok and rl_action in {Action.BUY, Action.SELL, Action.CLOSE}:
            order = self.executor.execute(symbol, rl_action, quantity)
            self.risk.apply_fill(exposure_delta=quantity * 2)

        return {
            "snapshot": snapshot.__dict__,
            "features": features,
            "decision": decision.__dict__ | {"action": decision.action.value, "regime": decision.regime.value},
            "order": order,
            "risk_state": self.risk.state.__dict__,
        }

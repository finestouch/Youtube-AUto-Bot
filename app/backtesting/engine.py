from __future__ import annotations

from app.core.orchestrator import TradingOrchestrator


class BacktestEngine:
    def __init__(self, orchestrator: TradingOrchestrator | None = None) -> None:
        self.orchestrator = orchestrator or TradingOrchestrator()

    def run_historical(self, symbol: str = "BTCUSDT", periods: int = 50) -> dict:
        results = [self.orchestrator.run_cycle(symbol=symbol, quantity=0.05) for _ in range(periods)]
        executed = sum(1 for r in results if r["order"])
        return {"periods": periods, "executed_trades": executed, "paper_pnl_proxy": executed * 0.15}

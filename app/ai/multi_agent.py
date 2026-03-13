from __future__ import annotations

from dataclasses import dataclass

from app.core.models import Action


@dataclass
class AgentVote:
    agent: str
    vote: bool
    reason: str


class MultiAgentSignalEngine:
    AGENTS = [
        "trend_agent",
        "momentum_agent",
        "orderbook_agent",
        "ai_forecast_agent",
        "whale_agent",
        "sniper_agent",
        "liquidity_trap_agent",
    ]

    def evaluate(self, features: dict[str, float]) -> tuple[list[AgentVote], bool]:
        votes: list[AgentVote] = [
            AgentVote("trend_agent", features["trend_strength"] > 0.2, "trend strength"),
            AgentVote("momentum_agent", features["momentum_score"] > 0.1, "momentum"),
            AgentVote("orderbook_agent", features["orderbook_imbalance"] > 0.1, "orderbook imbalance"),
            AgentVote("ai_forecast_agent", features["momentum_score"] + features["trend_strength"] > 0.2, "forecast edge"),
            AgentVote("whale_agent", features["btc_dominance"] < 57, "whale activity proxy"),
            AgentVote("sniper_agent", features["volatility_index"] > 0.55, "high-opportunity volatility"),
            AgentVote("liquidity_trap_agent", not (features["liquidity_pressure"] > 0.85), "trap detection"),
        ]
        liquidity_trap = features["liquidity_pressure"] > 0.85
        return votes, liquidity_trap

    @staticmethod
    def infer_action(vote_count: int, threshold: int) -> Action:
        return Action.BUY if vote_count >= threshold else Action.HOLD

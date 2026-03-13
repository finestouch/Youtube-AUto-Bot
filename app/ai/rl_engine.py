from __future__ import annotations

from app.core.models import Action


class ReinforcementLearningDecisionEngine:
    """Policy ensemble placeholder for PPO + DQN + SAC outputs."""

    def score_action(self, features: dict[str, float], proposed: Action) -> tuple[Action, float]:
        base = (features["trend_strength"] + features["momentum_score"] + 1) / 3
        confidence = max(0.0, min(1.0, base))
        if features["volatility_index"] > 0.95:
            return Action.CLOSE, 0.75
        if confidence < 0.33:
            return Action.HOLD, confidence
        return proposed, confidence

from __future__ import annotations

from app.core.models import Regime


class MarketRegimeDetector:
    """Hybrid detector placeholder for HMM + RF + NN voting."""

    def classify(self, features: dict[str, float]) -> Regime:
        if features["volatility_index"] > 0.9 and features["momentum_score"] < -0.5:
            return Regime.CRASH_RISK
        if features["trend_strength"] > 0.3:
            return Regime.TRENDING
        if features["volatility_index"] > 0.75:
            return Regime.HIGH_VOL
        return Regime.SIDEWAYS

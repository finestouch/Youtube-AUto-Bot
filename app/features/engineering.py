from __future__ import annotations

import math

from app.core.models import MarketSnapshot


class FeatureEngineer:
    def build(self, m: MarketSnapshot) -> dict[str, float]:
        trend_strength = math.tanh((m.price - 60000) / 5000)
        momentum_score = math.tanh((m.funding_rate * 20) + m.sentiment_score)
        volatility_index = min(1.0, abs(m.bid_ask_imbalance) + (m.volume / 10000))
        return {
            "trend_strength": trend_strength,
            "momentum_score": momentum_score,
            "volatility_index": volatility_index,
            "orderbook_imbalance": m.bid_ask_imbalance,
            "sentiment_score": m.sentiment_score,
            "liquidity_pressure": 1 - abs(m.bid_ask_imbalance),
            "funding_rate": m.funding_rate,
            "btc_dominance": m.btc_dominance,
        }

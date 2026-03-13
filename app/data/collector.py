from __future__ import annotations

import random
from datetime import datetime

from app.core.models import MarketSnapshot


class DataCollector:
    """Data edge layer stub: market microstructure, on-chain, sentiment, cross-market signals."""

    def collect(self, symbol: str = "BTCUSDT") -> MarketSnapshot:
        price = random.uniform(50000, 70000)
        volume = random.uniform(1000, 10000)
        return MarketSnapshot(
            symbol=symbol,
            price=price,
            volume=volume,
            bid_ask_imbalance=random.uniform(-1, 1),
            funding_rate=random.uniform(-0.03, 0.03),
            btc_dominance=random.uniform(45, 60),
            sentiment_score=random.uniform(-1, 1),
            timestamp=datetime.utcnow(),
        )

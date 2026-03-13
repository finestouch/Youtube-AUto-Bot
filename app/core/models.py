from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Regime(str, Enum):
    TRENDING = "trending"
    SIDEWAYS = "sideways"
    HIGH_VOL = "high_volatility"
    CRASH_RISK = "crash_risk"


class Action(str, Enum):
    BUY = "buy"
    SELL = "sell"
    HOLD = "hold"
    CLOSE = "close"


@dataclass
class MarketSnapshot:
    symbol: str
    price: float
    volume: float
    bid_ask_imbalance: float
    funding_rate: float
    btc_dominance: float
    sentiment_score: float
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class EngineDecision:
    action: Action
    confidence: float
    regime: Regime
    votes: int
    blocked: bool
    reasons: list[str]


@dataclass
class Position:
    symbol: str
    side: str
    quantity: float
    entry_price: float
    current_price: float


@dataclass
class RiskState:
    current_exposure_pct: float
    daily_pnl_pct: float
    trading_enabled: bool

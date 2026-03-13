from __future__ import annotations

from app.core.config import settings
from app.core.models import Action, RiskState


class RiskManager:
    def __init__(self) -> None:
        self.state = RiskState(current_exposure_pct=0.0, daily_pnl_pct=0.0, trading_enabled=True)

    def can_trade(self, action: Action, confidence: float) -> tuple[bool, str]:
        if not self.state.trading_enabled:
            return False, "trading disabled"
        if self.state.daily_pnl_pct <= -settings.daily_loss_limit_percent:
            if settings.auto_shutdown_on_drawdown:
                self.state.trading_enabled = False
            return False, "daily drawdown limit reached"
        if action in {Action.BUY, Action.SELL} and confidence < 0.55:
            return False, "confidence too low"
        if self.state.current_exposure_pct >= settings.max_portfolio_exposure_percent:
            return False, "max exposure reached"
        return True, "risk checks passed"

    def apply_fill(self, exposure_delta: float, pnl_delta: float = 0.0) -> RiskState:
        self.state.current_exposure_pct = max(0.0, self.state.current_exposure_pct + exposure_delta)
        self.state.daily_pnl_pct += pnl_delta
        return self.state

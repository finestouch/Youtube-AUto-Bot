from __future__ import annotations

from app.core.models import RiskState


class TelegramBotInterface:
    """Minimal Telegram adapter; wire this into python-telegram-bot handlers in production."""

    def __init__(self) -> None:
        self.enabled = True

    def available_commands(self) -> list[str]:
        return [
            "/start",
            "/balance",
            "/positions",
            "/enable_trading",
            "/disable_trading",
            "/sniper_mode",
            "/whale_watch",
            "/performance",
            "/risk_settings",
        ]

    def render_risk_settings(self, state: RiskState) -> str:
        return (
            f"Trading: {'ON' if state.trading_enabled else 'OFF'} | "
            f"Exposure: {state.current_exposure_pct:.2f}% | Daily PnL: {state.daily_pnl_pct:.2f}%"
        )

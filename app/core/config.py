from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "Autonomous AI Crypto Trading Super Machine"
    env: str = "dev"
    exchange_base_url: str = "https://api.binance.com"
    telegram_token: str = ""
    telegram_chat_id: str = ""

    max_risk_per_trade_percent: float = Field(default=1.0, ge=0.1, le=5.0)
    max_portfolio_exposure_percent: float = Field(default=20.0, ge=1.0, le=100.0)
    daily_loss_limit_percent: float = Field(default=5.0, ge=1.0, le=20.0)
    auto_shutdown_on_drawdown: bool = True

    min_votes_required: int = 4
    block_on_liquidity_trap: bool = True


settings = Settings()

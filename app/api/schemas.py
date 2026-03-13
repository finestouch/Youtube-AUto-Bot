from pydantic import BaseModel, Field


class CycleRequest(BaseModel):
    symbol: str = Field(default="BTCUSDT")
    quantity: float = Field(default=0.1, gt=0)


class ToggleTradingRequest(BaseModel):
    enabled: bool

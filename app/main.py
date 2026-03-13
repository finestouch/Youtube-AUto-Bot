from fastapi import FastAPI

from app.api.schemas import CycleRequest, ToggleTradingRequest
from app.core.config import settings
from app.core.orchestrator import TradingOrchestrator
from app.telegram.interface import TelegramBotInterface

app = FastAPI(title=settings.app_name)
engine = TradingOrchestrator()
telegram = TelegramBotInterface()


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": settings.app_name}


@app.post("/trade/cycle")
def trade_cycle(req: CycleRequest) -> dict:
    return engine.run_cycle(symbol=req.symbol, quantity=req.quantity)


@app.get("/telegram/commands")
def commands() -> dict:
    return {"commands": telegram.available_commands()}


@app.post("/trading/toggle")
def toggle(req: ToggleTradingRequest) -> dict:
    engine.risk.state.trading_enabled = req.enabled
    return {"trading_enabled": engine.risk.state.trading_enabled}


@app.get("/risk")
def risk_state() -> dict:
    return engine.risk.state.__dict__

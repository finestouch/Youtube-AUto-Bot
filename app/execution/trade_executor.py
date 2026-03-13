from __future__ import annotations

from datetime import datetime

from app.core.models import Action


class TradeExecutor:
    def __init__(self) -> None:
        self.orders: list[dict] = []

    def execute(self, symbol: str, action: Action, quantity: float, order_type: str = "limit") -> dict:
        order = {
            "symbol": symbol,
            "action": action.value,
            "quantity": quantity,
            "order_type": order_type,
            "status": "filled" if action != Action.HOLD else "ignored",
            "slippage_bps": 2,
            "split_orders": quantity > 1,
            "timestamp": datetime.utcnow().isoformat(),
        }
        self.orders.append(order)
        return order

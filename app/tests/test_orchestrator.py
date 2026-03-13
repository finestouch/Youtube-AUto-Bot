from app.core.orchestrator import TradingOrchestrator
from app.security.crypto import Aes256Cipher


def test_cycle_returns_decision_structure() -> None:
    payload = TradingOrchestrator().run_cycle()
    assert "decision" in payload
    assert payload["decision"]["action"] in {"buy", "sell", "hold", "close"}
    assert payload["decision"]["votes"] >= 0


def test_aes256_roundtrip() -> None:
    cipher = Aes256Cipher()
    secret = "super-secret-key"
    encrypted = cipher.encrypt(secret)
    assert encrypted != secret
    assert cipher.decrypt(encrypted) == secret

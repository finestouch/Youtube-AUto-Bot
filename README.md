# Autonomous AI Crypto Trading Super Machine

Production-oriented Python platform for autonomous crypto trading using:
- Multi-source data edge signals (microstructure, sentiment, cross-market)
- Regime detection + multi-agent voting + RL decision layer
- Risk-first execution controls and auto-shutdown on drawdown
- FastAPI control plane and Telegram command surface
- Backtesting/paper-trading scaffolding, Docker deployment

## Architecture

- `app/data/collector.py`: data edge ingestion abstraction
- `app/features/engineering.py`: derived features (`trend_strength`, `momentum_score`, etc.)
- `app/ai/regime_detector.py`: regime classification (trending/sideways/high-vol/crash)
- `app/ai/multi_agent.py`: 7-agent vote stack + liquidity trap blocking
- `app/ai/rl_engine.py`: PPO/DQN/SAC-style policy ensemble placeholder
- `app/risk/manager.py`: risk limits and shutdown logic
- `app/execution/trade_executor.py`: execution engine (market/limit/stop-limit extensible)
- `app/telegram/interface.py`: Telegram command interface contract
- `app/core/orchestrator.py`: autonomous cycle orchestrator
- `app/main.py`: FastAPI endpoints

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp .env.example .env
uvicorn app.main:app --reload
```

## API Endpoints

- `GET /health`
- `POST /trade/cycle` `{ "symbol": "BTCUSDT", "quantity": 0.1 }`
- `GET /telegram/commands`
- `POST /trading/toggle` `{ "enabled": true }`
- `GET /risk`

## Safety Controls

- Max risk/trade, max exposure, daily drawdown limit
- Liquidity trap detection can block entries
- Confidence gating from RL layer
- AES-256-GCM helper for key encryption at rest (`app/security/crypto.py`)

## Deployment

### Docker
```bash
docker compose up --build
```

### Cloud
Deploy container to AWS ECS/Fargate or Google Cloud Run. Keep secrets in AWS Secrets Manager or GCP Secret Manager and inject as environment variables.

## Testing

```bash
pytest
python scripts/run_backtest.py
```

## Production Hardening Roadmap

1. Wire real exchange SDKs (Binance/Bybit/Coinbase), websockets, and persistent storage.
2. Replace heuristics with trained HMM/RF/NN and policy checkpoints.
3. Add full 2FA admin panel for command operations.
4. Add canary forward-testing and shadow execution mode.
5. Add robust observability (Prometheus/Grafana/OpenTelemetry).

from app.backtesting.engine import BacktestEngine

if __name__ == "__main__":
    report = BacktestEngine().run_historical(periods=20)
    print(report)

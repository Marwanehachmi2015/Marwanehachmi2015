"""
Configuration file for gold trading bot
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===== API Settings =====
ALPHA_VANTAGE_KEY = os.getenv('ALPHA_VANTAGE_KEY', 'your_key_here')
FINNHUB_KEY = os.getenv('FINNHUB_KEY', 'your_key_here')
ALPACA_API_KEY = os.getenv('ALPACA_API_KEY', 'your_key_here')
ALPACA_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY', 'your_key_here')
ALPACA_BASE_URL = os.getenv('ALPACA_BASE_URL', 'https://paper-trading-api.alpaca.markets')

# ===== Trading Configuration =====
TRADING_CONFIG = {
    'symbol': 'GC=F',  # Gold Futures
    'timeframe': '1h',  # 1 hour
    'initial_balance': 10000,  # Initial capital
    'max_position_size': 0.1,  # 10% of balance per trade
    'risk_percentage': 2,  # 2% risk per trade
}

# ===== Technical Indicators Configuration =====
INDICATORS_CONFIG = {
    'sma_short': 20,  # Short-term Simple Moving Average
    'sma_long': 50,   # Long-term Simple Moving Average
    'ema_short': 12,  # Short-term Exponential Moving Average
    'ema_long': 26,   # Long-term Exponential Moving Average
    'rsi_period': 14,  # Relative Strength Index period
    'macd_fast': 12,   # MACD fast line
    'macd_slow': 26,   # MACD slow line
    'macd_signal': 9,  # MACD signal line
    'bollinger_period': 20,
    'bollinger_std_dev': 2,
}

# ===== Risk Management Settings =====
RISK_MANAGEMENT = {
    'stop_loss_percentage': 2.0,   # Stop loss at 2%
    'take_profit_percentage': 5.0,  # Take profit at 5%
    'trailing_stop_percentage': 1.5,  # Trailing stop at 1.5%
    'max_daily_loss': 5.0,  # Maximum daily loss 5%
    'max_open_positions': 3,  # Maximum concurrent positions
}

# ===== Monitoring Settings =====
MONITORING = {
    'check_interval': 60,  # Check interval in seconds
    'log_level': 'INFO',
    'send_alerts': True,
    'alert_email': os.getenv('ALERT_EMAIL', 'your_email@gmail.com'),
}

# ===== Database Configuration =====
DATABASE = {
    'type': 'sqlite',  # sqlite or postgresql
    'path': 'data/trading_bot.db',
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 5432),
    'user': os.getenv('DB_USER', 'user'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'database': os.getenv('DB_NAME', 'gold_trading'),
}

# ===== Advanced Settings =====
ADVANCED_SETTINGS = {
    'use_machine_learning': False,  # Use ML for predictions
    'backtest_mode': False,  # Backtest historical data
    'paper_trading': True,  # Paper trading mode (no real money)
    'simulate_slippage': True,  # Simulate price slippage
}

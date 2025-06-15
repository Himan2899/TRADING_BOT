# Binance Futures Trading Bot

A simplified trading bot for Binance Futures Testnet that supports market, limit, and stop-limit orders.

## Features

- Support for market, limit, and stop-limit orders
- Command-line interface for easy interaction
- Comprehensive error handling and logging
- Account balance and position information
- Testnet support for safe testing

## Prerequisites

- Python 3.7+
- Binance Testnet account
- API credentials from Binance Testnet

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd tradingbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your API credentials:
```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
TESTNET=True
```

## Usage

### Market Order
```bash
python main.py --type MARKET --side BUY --quantity 0.001 --symbol BTCUSDT
```

### Limit Order
```bash
python main.py --type LIMIT --side SELL --quantity 0.001 --price 50000 --symbol BTCUSDT
```

### Stop-Limit Order
```bash
python main.py --type STOP_LIMIT --side BUY --quantity 0.001 --price 49000 --stop-price 50000 --symbol BTCUSDT
```

## Available Options

- `--symbol`: Trading pair symbol (default: BTCUSDT)
- `--quantity`: Order quantity (default: 0.001)
- `--price`: Limit order price (required for LIMIT and STOP_LIMIT orders)
- `--stop-price`: Stop price for stop-limit orders (required for STOP_LIMIT orders)
- `--side`: Order side (BUY or SELL)
- `--type`: Order type (MARKET, LIMIT, or STOP_LIMIT)

## Logging

The bot uses the `rich` library for beautiful console output and logging. All API requests, responses, and errors are logged for debugging purposes.

## Error Handling

The bot includes comprehensive error handling for:
- Invalid API credentials
- Network issues
- Invalid order parameters
- Insufficient balance
- Rate limiting

## Security Notes

- Never commit your `.env` file or expose your API credentials
- Always use testnet for testing
- Start with small order quantities
- Monitor your positions and orders regularly 
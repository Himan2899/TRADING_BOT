# 🚀 Binance Futures Trading Bot

A powerful and user-friendly trading bot for Binance Futures Testnet that supports multiple order types and provides real-time market data.

## 📋 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Order Types](#-order-types)
- [Error Handling](#-error-handling)
- [Security Notes](#-security-notes)
- [Troubleshooting](#-troubleshooting)

## ✨ Features

- 📊 Support for multiple order types:
  - Market orders
  - Limit orders
  - Stop-limit orders
- 💻 Command-line interface for easy interaction
- 📝 Comprehensive error handling and logging
- 💰 Account balance and position information
- 🔄 Testnet support for safe testing
- ⏰ Real-time market price checking
- 📈 Position tracking and management

## 🛠️ Prerequisites

- Python 3.7 or higher
- Binance Testnet account
- API credentials from Binance Testnet
- Basic understanding of cryptocurrency trading

## 📥 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd tradingbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

1. Create a `.env` file in the project root with your API credentials:
```env
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
TESTNET=True
```

2. Get your API credentials:
   - Visit [Binance Testnet](https://testnet.binance.vision/)
   - Create an account if you haven't already
   - Generate API keys from your account settings
   - Enable Futures trading permissions
   - Copy the API key and Secret key to your `.env` file

## 🚀 Usage

### Basic Commands

1. Check account balance:
```bash
python main.py --balance
```

2. Get current market price:
```bash
python main.py --mark-price --symbol BTCUSDT
```

3. Check server time:
```bash
python main.py --server-time
```

### Order Types

#### 1. Market Order
```bash
python main.py --type MARKET --side BUY --quantity 0.001 --symbol BTCUSDT
```

#### 2. Limit Order
```bash
python main.py --type LIMIT --side SELL --quantity 0.001 --price 50000 --symbol BTCUSDT
```

#### 3. Stop-Limit Order
```bash
python main.py --type STOP_LIMIT --side BUY --quantity 0.001 --price 49000 --stop-price 50000 --symbol BTCUSDT
```

## 📊 Command Options

| Option | Description | Required | Default |
|--------|-------------|----------|---------|
| `--symbol` | Trading pair symbol | No | BTCUSDT |
| `--quantity` | Order quantity | Yes* | 0.001 |
| `--price` | Limit order price | Yes** | - |
| `--stop-price` | Stop price for stop-limit orders | Yes*** | - |
| `--side` | Order side (BUY/SELL) | Yes | - |
| `--type` | Order type | Yes | - |
| `--balance` | Check account balance | No | - |
| `--mark-price` | Get current market price | No | - |
| `--server-time` | Get server time | No | - |

*Required for all order types
**Required for LIMIT and STOP_LIMIT orders
***Required for STOP_LIMIT orders

## ⚠️ Error Handling

The bot includes comprehensive error handling for:
- 🔑 Invalid API credentials
- 🌐 Network issues
- ❌ Invalid order parameters
- 💸 Insufficient balance
- ⏱️ Rate limiting
- 💰 Invalid price levels
- 📊 Invalid quantities

## 🔒 Security Notes

- Never commit your `.env` file or expose your API credentials
- Always use testnet for testing
- Start with small order quantities
- Monitor your positions and orders regularly
- Keep your API keys secure and rotate them periodically
- Enable IP restrictions on your API keys
- Use strong passwords for your Binance account

## 🔍 Troubleshooting

### Common Issues

1. **Invalid API Key Error**
   - Verify your API credentials in the `.env` file
   - Check if your API key has the correct permissions
   - Ensure you're using Testnet API keys

2. **Invalid Price Error**
   - Check current market price using `--mark-price`
   - For SELL orders: price must be higher than current price
   - For BUY orders: price must be lower than current price

3. **Invalid Quantity Error**
   - Check minimum quantity requirements for the symbol
   - Ensure you have sufficient balance
   - Verify quantity precision requirements

### Getting Help

If you encounter any issues:
1. Check the error message carefully
2. Verify your order parameters
3. Ensure you have sufficient balance
4. Check your internet connection
5. Verify API key permissions

## 📈 Best Practices

1. Always test with small quantities first
2. Monitor your positions regularly
3. Set appropriate stop-loss orders
4. Keep track of your trading history
5. Don't risk more than you can afford to lose
6. Keep your bot and dependencies updated
7. Regularly check for any API changes

## 🤝 Contributing

Feel free to submit issues and enhancement requests! 

🤝 Support
If you find this project helpful, please give it a ⭐️ on GitHub!

📞 Contact
For any queries or support, please reach out to us through:

Email: himanshuofficialuserid@gmail.com
Developed with ❤️ by Himanshu Bali 💻👨‍💻🚀

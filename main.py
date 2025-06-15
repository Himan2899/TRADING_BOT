import argparse
from rich.console import Console
from rich.table import Table
from trading_bot import TradingBot
from config import settings
from logger import logger

console = Console()

def display_order(order):
    """Display order information in a formatted table."""
    table = Table(title="Order Information")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")
    
    for key, value in order.items():
        table.add_row(str(key), str(value))
    
    console.print(table)

def display_balance(balance_info):
    """Display account balance information in a formatted table."""
    table = Table(title="Account Balance")
    table.add_column("Asset", style="cyan")
    table.add_column("Wallet Balance", style="green")
    table.add_column("Cross Wallet Balance", style="yellow")
    table.add_column("Available Balance", style="magenta")

    for item in balance_info:
        table.add_row(
            item.get('asset', 'N/A'),
            item.get('walletBalance', 'N/A'),
            item.get('crossWalletBalance', 'N/A'),
            item.get('availableBalance', 'N/A')
        )
    console.print(table)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", default=settings.DEFAULT_SYMBOL, help="Trading pair symbol")
    parser.add_argument("--quantity", type=float, default=settings.DEFAULT_QUANTITY, help="Order quantity")
    parser.add_argument("--price", type=float, help="Limit order price")
    parser.add_argument("--stop-price", type=float, help="Stop price for stop-limit orders")
    parser.add_argument("--side", choices=["BUY", "SELL"], help="Order side (required for placing orders)")
    parser.add_argument("--type", choices=["MARKET", "LIMIT", "STOP_LIMIT"], help="Order type (required for placing orders)")
    parser.add_argument("--time-in-force", choices=["GTC", "IOC", "FOK"], default="GTC", help="Time in force for limit orders")
    parser.add_argument("--balance", action="store_true", help="Check account balance")
    parser.add_argument("--server-time", action="store_true", help="Get Binance server time")
    parser.add_argument("--mark-price", action="store_true", help="Get current mark price for a symbol")
    
    args = parser.parse_args()
    
    try:
        # Initialize the trading bot
        bot = TradingBot(settings.API_KEY, settings.API_SECRET, settings.TESTNET)
        
        if args.balance:
            balance = bot.get_account_balance()
            display_balance(balance)
        elif args.server_time:
            bot.get_server_time()
        elif args.mark_price:
            if not args.symbol:
                raise ValueError("Symbol is required to get mark price")
            bot.get_mark_price(args.symbol)
        elif args.side and args.type:
            # Place the order based on type
            if args.type == "MARKET":
                order = bot.place_market_order(args.symbol, args.side, args.quantity)
            elif args.type == "LIMIT":
                if not args.price:
                    raise ValueError("Price is required for limit orders")
                order = bot.place_limit_order(
                    args.symbol, 
                    args.side, 
                    args.quantity, 
                    args.price
                )
            elif args.type == "STOP_LIMIT":
                if not args.price or not args.stop_price:
                    raise ValueError("Price and stop price are required for stop-limit orders")
                order = bot.place_stop_limit_order(
                    args.symbol, 
                    args.side, 
                    args.quantity, 
                    args.price, 
                    args.stop_price
                )
            
            # Display order information
            display_order(order)
        else:
            parser.print_help()
            logger.warning("Please specify an order type and side, or use --balance to check account.")
        
    except Exception as e:
        logger.error(f"Error: {e}")
        raise

if __name__ == "__main__":
    main() 
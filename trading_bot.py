from binance.client import Client
from binance.exceptions import BinanceAPIException
from typing import Dict, Optional, Union
from decimal import Decimal
import time
from logger import logger
from config import settings

class TradingBot:
    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
        """Initialize the trading bot with API credentials."""
        self.client = Client(api_key, api_secret, testnet=testnet)
        logger.info(f"Trading bot initialized with testnet={testnet}")

    def place_market_order(self, symbol: str, side: str, quantity: float) -> Dict:
        """Place a market order."""
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logger.info(f"Market order placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Error placing market order: {e}")
            raise

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float) -> Dict:
        """Place a limit order."""
        try:
            # Get symbol info to validate quantity and price
            symbol_info = self.client.futures_exchange_info()
            symbol_info = next((s for s in symbol_info['symbols'] if s['symbol'] == symbol), None)
            
            if not symbol_info:
                raise ValueError(f"Symbol {symbol} not found")

            # Format quantity and price according to symbol rules
            quantity_precision = symbol_info['quantityPrecision']
            price_precision = symbol_info['pricePrecision']
            
            quantity = float(format(quantity, f'.{quantity_precision}f'))
            price = float(format(price, f'.{price_precision}f'))

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            logger.info(f"Limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Error placing limit order: {e}")
            raise

    def place_stop_limit_order(self, symbol: str, side: str, quantity: float, 
                             price: float, stop_price: float) -> Dict:
        """Place a stop-limit order."""
        try:
            # Get symbol info to validate quantity and price
            symbol_info = self.client.futures_exchange_info()
            symbol_info = next((s for s in symbol_info['symbols'] if s['symbol'] == symbol), None)
            
            if not symbol_info:
                raise ValueError(f"Symbol {symbol} not found")

            # Format quantity and price according to symbol rules
            quantity_precision = symbol_info['quantityPrecision']
            price_precision = symbol_info['pricePrecision']
            
            quantity = float(format(quantity, f'.{quantity_precision}f'))
            price = float(format(price, f'.{price_precision}f'))
            stop_price = float(format(stop_price, f'.{price_precision}f'))

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='STOP_LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price,
                stopPrice=stop_price
            )
            logger.info(f"Stop-limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Error placing stop-limit order: {e}")
            raise

    def get_order_status(self, symbol: str, order_id: int) -> Dict:
        """Get the status of an order."""
        try:
            order = self.client.futures_get_order(symbol=symbol, orderId=order_id)
            logger.info(f"Order status: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Error getting order status: {e}")
            raise

    def cancel_order(self, symbol: str, order_id: int) -> Dict:
        """Cancel an existing order."""
        try:
            result = self.client.futures_cancel_order(symbol=symbol, orderId=order_id)
            logger.info(f"Order cancelled: {result}")
            return result
        except BinanceAPIException as e:
            logger.error(f"Error cancelling order: {e}")
            raise

    def get_account_balance(self) -> Dict:
        """Get the account balance."""
        try:
            balance = self.client.futures_account_balance()
            logger.info(f"Account balance: {balance}")
            return balance
        except BinanceAPIException as e:
            logger.error(f"Error getting account balance: {e}")
            raise

    def get_position_info(self, symbol: Optional[str] = None) -> Dict:
        """Get position information."""
        try:
            positions = self.client.futures_position_information(symbol=symbol)
            logger.info(f"Position information: {positions}")
            return positions
        except BinanceAPIException as e:
            logger.error(f"Error getting position information: {e}")
            raise

    def get_server_time(self) -> Dict:
        """Get the Binance server time."""
        try:
            server_time = self.client.get_server_time()
            logger.info(f"Binance Server Time: {server_time}")
            return server_time
        except BinanceAPIException as e:
            logger.error(f"Error getting server time: {e}")
            raise

    def get_mark_price(self, symbol: str) -> float:
        """Get the current mark price for a symbol."""
        try:
            mark_price = self.client.futures_mark_price(symbol=symbol)
            price = float(mark_price['markPrice'])
            logger.info(f"Current Mark Price for {symbol}: {price}")
            return price
        except BinanceAPIException as e:
            logger.error(f"Error getting mark price for {symbol}: {e}")
            raise 
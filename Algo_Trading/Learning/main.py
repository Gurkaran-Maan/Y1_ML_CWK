from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderClass, TimeInForce, QueryOrderStatus
from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime

trading_client = TradingClient('PKVUSRS45ZL3QS0BJGUZ', 'y9IgdPrwc531n5hjNd2NRfcfRwXhzSsRwv4MzLLc', paper=True)

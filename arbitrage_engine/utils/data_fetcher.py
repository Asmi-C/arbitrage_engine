import yfinance as yf
import pandas as pd
from datetime import datetime

class DataFetcher:
    def __init__(self, tickers: list):
        self.tickers = tickers
        
    def fetch_realtime(self):
        """Fetch real-time data with 5ms latency"""
        data = yf.download(
            tickers=self.tickers,
            period="1d",
            interval="1m",
            prepost=True,
            threads=True
        )
        return data.pct_change().dropna()
    
    def fetch_historical(self, days=365):
        """For cointegration testing"""
        return yf.download(self.tickers, period=f"{days}d")['Close']
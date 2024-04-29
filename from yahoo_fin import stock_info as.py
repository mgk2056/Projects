from yahoo_fin import stock_info as si
import yfinance as yf
import pandas as pd

tickers = ('AAPL', 'MSFT', 'IBM')

infos = []
for i in tickers:
    infos.append(yf.Ticker(i).info)
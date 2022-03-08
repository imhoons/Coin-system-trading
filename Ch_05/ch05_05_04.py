# ch05/05_04.py
import pybithumb
import time

tickers = pybithumb.get_tickers()
for ticker in tickers:
    price = pybithumb.get_current_price(ticker)
    print(price, ticker)
    time.sleep(0.1)
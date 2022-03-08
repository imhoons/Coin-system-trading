# ch05/05_01.py
import pybithumb

tickers = pybithumb.get_tickers()
print(tickers)
print(len(tickers))

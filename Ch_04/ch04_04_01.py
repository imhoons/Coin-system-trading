# ch04/04_01.py
import requests

url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text
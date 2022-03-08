# ch04/04_연습문제.py
from pandas import DataFrame, Series

#1
data = {'open':[737, 750, 770],'high':[755, 780, 770], 'low':[700,710,750], 'close':[750, 770, 730]}
date = ["2018-01-01", "2018-01-02", "2018-01-03"]
df= DataFrame(data, index = date)
print(df)

#2
volatility = Series([55, 70, 20], index = date)  #인덱스 지정 꼭 해줘야함!!!
df['volatility'] = volatility
print(df)


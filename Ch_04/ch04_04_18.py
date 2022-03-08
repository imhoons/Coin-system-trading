# ch04/04_18.py
import pandas as pd
df = pd.read_excel("C:\\Users\\전지훈\\Desktop\\Bitcoin python\\Ch_04\\ohlc.xlsx")
df = df.set_index('date')
print(df)
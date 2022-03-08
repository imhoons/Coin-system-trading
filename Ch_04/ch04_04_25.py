# ch04/04_25.py
from pandas import Series

s = Series([100,200,300])
s2 = s.shift(1)
s3 = s.shift(-1)
print(s)
print(s2)
print(s3)


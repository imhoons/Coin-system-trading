# ch04/04_22.py
from pandas import DataFrame
data={'open':[730, 750], 'high':[755, 780], "low":[700,710], "close":[750, 770]}
df=DataFrame(data, index=["2018-01-01", "2018-01-02"])
print(df.loc["2018-01-01"])
print(df.iloc[0])

target=["2018-01-01", "2018-01-02"]
print(df.loc[target])

#행은 loc, iloc 열은 그냥 열이름
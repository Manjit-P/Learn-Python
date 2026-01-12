import pandas as pd

'''data = [100, 102, 104, 200, 202]

series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
#print(series.iloc[0:2])
#print(series.loc['a'])
print(series[series < 200])'''

name = ['hello', 'world', 'how']

series = pd.Series(name, index = [1, 2, 3])
print(series)
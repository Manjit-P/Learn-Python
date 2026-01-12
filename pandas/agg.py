# aggregate function = reduces a set of values into a single summary value 
#                      used to summarize and analyze data 
#                      often used with the groupby() function

import pandas as pd

df = pd.read_csv('pandas/data.csv')
#whole dataframe
#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.count())

#single column
#print(df['Height'].mean())
#print(df['Height'].sum())
#print(df['Height'].min())
#print(df['height].max())
#print(df["Height"].count())

group = df.groupby("Type1")

print(group["Height"].mean())
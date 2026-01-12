import pandas as pd

df = pd.read_csv("data.csv", index_col='Name')

#Selection by column
#print(df['Name'].to_string())
#print(df[['Name','Height', 'Weight']].to_string())

#print(df.loc['Charizard': 'Blastoise', ['Height', 'Weight']])
pokemon = input("Enter a pokemon name: ")
try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")
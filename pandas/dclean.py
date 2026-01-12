import pandas as pd

df = pd.read_csv("pandas/data.csv")

#drop irrevalent column
#df = df.drop(columns=['Type1'])

# drop not available 
#df = df.dropna(subset=['Type2'])

#fill not available
#df = df.fillna({'Type2': 'None'})

#fix inconsistent data
#df['Type1'] = df['Type1'].replace({'Grass': "GRASS", 'Fire': 'FIRE'})

#standardize text
#df["Name"] = df["Name"].str.upper()

#fix data
#df["Legendary"] = df["Legendary"].astype(bool)

#remove duplicate values
df = df.drop_duplicates()
print(df.to_string())
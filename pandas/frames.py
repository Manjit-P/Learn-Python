import pandas as pd

data = {
    'name' : ['Spongebob', 'Patrick', 'Squidward'],
    'age' : [30, 35, 50]
}

df = pd.DataFrame(data, index =[1, 2, 3])

#add a new column
df['job'] = ['cook', 'N/A', 'Cashier']
#add new rows
new_rows = pd.DataFrame([{"name": 'Sandy', 'age' : '28', 'job' : 'scientist'},{"name": 'Eugene', 'age' : '60', 'job' : 'Manager'}], index=[4,5])
df = pd.concat([df,new_rows])
print(df)

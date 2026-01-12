import pandas as pd

url = "https://halgorithm.com/resources/courses/machine-learning-foundations/bookstore_sales.csv"
df = pd.read_csv(url)
print(df.head())

# Reflection Questions:

# 1: A boolean filter lets you select only the rows that match a certain condition. 
# For example, I can filter the sales data to only show orders from the South region.
# 2: df["revenue"] returns one column as a Series, while df[["revenue"]] returns the 
# column as a DataFrame. This matters when doing calculations or when I need to work
# with multiple columns.
# 3: I would choose pandas because it makes it easier and faster to organize, filter, 
# and analyze large amounts of data without having to do everything manually like in Excel.

print("--- Exercise 1 ---")

import pandas as pd

df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("--- Exercise 2 ---")

south = df[df['region'] == 'South']
print(len(south))
print(south.head())

print("--- Exercise 3 ---")

top_five = df.sort_values('revenue', ascending=False).head(5)
print(top_five)
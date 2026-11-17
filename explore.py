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

print("--- Exercise 4 ---")

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head())

print("--- Exercise 5 ---")

df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())

print("--- Exercise 6 ---")

print(df['region'].unique())
print(df['region'].value_counts())

print("--- Exercise 7 ---")

selected_columns = df[['region', 'product', 'revenue']]
print(selected_columns.head())
print(selected_columns.shape)

print("--- Exercise 8 ---")

df.to_csv('data/explored.csv', index=False)
print("The explored.csv file has been saved successfully!")
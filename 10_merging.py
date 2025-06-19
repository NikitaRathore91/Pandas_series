#pd.merge(left, right, how='inner', on='key') 
# Parameter	Purpose
# left, right	The DataFrames to merge
# how	Type of join: 'inner', 'outer', 'left', 'right'
# on	Column name(s) to join on
# left_on, right_on	If the join keys have different names in both DataFrames
# suffixes	Add suffixes to overlapping column names


# | Join Type | Description                                       |
# | --------- | ------------------------------------------------- |
# | `'inner'` | Only matching rows from both DataFrames           |
# | `'left'`  | All rows from left + matching from right          |
# | `'right'` | All rows from right + matching from left          |
# | `'outer'` | All rows from both; fill NaNs for missing matches |


import pandas as pd

df1 = pd.DataFrame({
    'EmployeeID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'EmployeeID': [2, 3, 4],
    'Department': ['HR', 'IT', 'Finance']
})

merged = pd.merge(df1, df2, on='EmployeeID', how='inner')
print(merged)


# If your key columns have different names:
# pd.merge(df1, df2, left_on='id1', right_on='id2')
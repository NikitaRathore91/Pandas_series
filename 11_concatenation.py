# In Pandas, concatenation is used to combine DataFrames or Series along a particular axis (rows or columns). The main function for this is pd.concat().
#pd.concat(objs, axis=0, join='outer', ignore_index=False)
# objs: List of Series or DataFrames to concatenate.
# axis: 0 to concatenate along rows (default), 1 to concatenate along columns.
# join: 'outer' (default) keeps all columns; 'inner' keeps only common ones.
# ignore_index: If True, ignores original index and resets.


import pandas as pd
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

df_concat = pd.concat([df1,df2],axis=0,ignore_index=True)
print(df_concat)

# for axis = 0
#    A  B
# 0  1  3
# 1  2  4
# 2  5  7
# 3  6  8

# for axis = 1
#    0  1  2  3
# 0  1  3  5  7
# 1  2  4  6  8 n
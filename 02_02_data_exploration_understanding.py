'''viewing first or last 5 rows :- head(), tail()
#head() :- by default it will show top 5 rows
#head(n):- top n rows
#tail():- last 5 rows
#tail(n) ;- last 5 rows '''

import pandas as pd
df = pd.read_json("sample_Data.json")

#print("printing top 10 values of .json file")
#print(df.head(10))

#rint("printing last 10 values of .json file")
#print(df.tail(10))


""" df.info() — What it shows:
It prints a summary of the DataFrame, including:
Number of rows and columns
Column names
Number of non-null values in each column
Data types of each column (int64, float64, object, etc.)
Memory usage"""

print("Displaying info of the data set")
print(df.info())    

"""f.shape	Shows (rows, columns)
df.columns	Shows column names
print(f'...')	Prints info nicely using f-string"""

print(f'Shape is->(row,col): {df.shape}')
print(f'Column Names are ->  : {df.columns}')

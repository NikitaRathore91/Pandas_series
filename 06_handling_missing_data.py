""" 
NaN (Not a Number)
None (for object data types)

isnull() :- return true/false
true:- its null,false = not null
"""
import pandas as pd

data = {
    "Name" : ["Ram","Shyam","jake","Andrew","Kate","Aditi","Neha",None],
    "Age" : [22,None,30,50,78,45,50,60],
    "Salary" : [20000,None,30000,35000,32000,50000,60000,45000],
    "score" :[80,None,88,90,89,95,70,75]
}
"""---------------df.isnull(),,,,,,df.dropna()----------------------"""
df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum()) #tells total number of nulll values per column

#print(df.dropna(inplace=True)) #It removes any rows in the DataFrame that contain missing values
print(df)

""" 
df.dropna(axis=1)         # Drop columns with any NaN
df.dropna(how='all')      # Drop rows only if all values are NaN
df.dropna(subset=['Age']) # Drop rows where 'Age' is NaN
df.dropna(inplace=True)   # Modify the DataFrame in place
"""


''' ---------------df.fillna()----------------'''
#df.fillna(0,inplace=True)
#print(df)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)

'''--------------INTERPOLATE()------------------ '''
#interpolate() fills missing (NaN) values using linear (or other) interpolation — 
#that is, it estimates values between known data points.
#df.interpolate(method='linear', inplace=False)

d = {
    'Age' : [22,None,30,50],
    'Salary' : [20000,None,30000,40000]
}

m = pd.DataFrame(d)
print(m)
m_interpolated = m.interpolate()
print(m_interpolated)

data = {
    "Time" : [1,2,3,4,5],
    "Value" : [20,None,30,None,50]
}
df = pd.DataFrame(data)
df["Value"] = df["Value"].interpolate(method="linear")
print(df)  

"""
  use of interpolaion
  1. timer series data
  2. numeric data with trends
  3. avoid dropping rows ,better use interpolation
"""
import pandas as pd

data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance'],
    'Salary': [50000, 60000, 45000, 52000, 48000],
    'Age': [25, 30, 28, 26, 25]
}

df = pd.DataFrame(data)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)
# o/P;-
# 25    98000
# 26    52000
# 28    45000
# 30    60000
# Name: Salary, dtype: int64
# Name: Salary, dtype: int64

""" GROUP BY IN MULTIPLE COLUMNS"""
grouped = df.groupby(["Age","Department"])["Salary"].sum()
print(grouped)
# Age  Department
# 25   Finance       48000
#      HR            50000
# 26   IT            52000
# 28   IT            45000
# 30   HR            60000
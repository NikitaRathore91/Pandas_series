''' Function	Description
sum()	Total
mean()	Average
count()	Number of non-null values
min()	Minimum
max()	Maximum
median()	Middle value
std()	Standard deviation '''

import pandas as pd

data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance'],
    'Salary': [40000, 45000, 60000, 62000, 50000],
    'Age': [25, 30, 28, 26, 35]
}

df = pd.DataFrame(data)

avg_salary = df['Salary'].mean()
print(avg_salary)
# a = df.agg(['sum', 'mean'])
a = df.select_dtypes(include='number').agg(['sum', 'mean'])
import pandas as pd

data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance'],
    'Salary': [40000, 45000, 60000, 62000, 50000],
    'Age': [25, 30, 28, 26, 35]
}

df = pd.DataFrame(data)

avg_salary = df['Salary'].mean()
print("Average Salary:", avg_salary)

# Correct aggregation
a = df[['Salary', 'Age']].agg(['sum', 'mean'])
# 0r a = df.select_dtypes(include='number').agg(['sum', 'mean'])
print(a)


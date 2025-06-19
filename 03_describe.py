import pandas as pd

data = {
    "Name" : ["Ram","Shyam","jake","Andrew","Kate","Aditi","Neha","Nikki"],
    "Age" : [22,20,30,50,78,45,50,60],
    "Salary" : [20000,25000,30000,35000,32000,50000,60000,45000],
    "performance score" :[80,79,88,90,89,95,70,75]
}

print("printing dataframe : ")
df = pd.DataFrame(data)
print(df)

print("printing descriptive statistics")
print(df.describe())

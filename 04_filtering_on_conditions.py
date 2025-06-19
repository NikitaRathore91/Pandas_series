""" 
1)-select specific columns
2)-filter rows
3)-combine multiple conditions

for selection of column we use square brackets
for selection of rows we use boolean brackets

selecting column return a series and a dataframe multiple columns of data

Syntax:-
column = df["column name"]
subset = df["colum1","column2"]

selecting rows
boolean indexing
#based on single condition
filtered_row = df[df["salary"]>50000]

#combine miltiple conditions
filtered_rows = df[(df["salary]>50000) & (df["column2"]<80000)]
"""
import pandas as pd
data = {
    "Name" : ["Ram","Shyam","jake","Andrew","Kate","Aditi","Neha","Nikki"],
    "Age" : [22,20,30,50,78,45,50,60],
    "Salary" : [20000,25000,30000,35000,32000,50000,60000,45000],
    "performance score" :[80,79,88,90,89,95,70,75]
}
 
df = pd.DataFrame(data)
print(df["Name"]) #will print name col
print(df[["Name","Age"]]) #selecting multiple columns

high_salary = df[df["Salary"]>50000] #filtering row with one condition
print(high_salary)  # will print -> 6 neha 50 60000 70

fil = df[(df["Salary"]>30000) & (df["Age"]>30)] #filtering row with multiple condition
print(fil)
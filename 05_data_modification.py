import pandas as pd
data = {
    "Name" : ["Ram","Shyam","jake","Andrew","Kate","Aditi","Neha","Nikki"],
    "Age" : [22,20,30,50,78,45,50,60],
    "Salary" : [20000,25000,30000,35000,32000,50000,60000,45000],
    "score" :[80,79,88,90,89,95,70,75]
}

df = pd.DataFrame(data)
print(df)

""" ---------------------ADDING A COLUMN--------------------------------------------"""

#syntax 1:- df["Col_name"] = some data
#adding new column in :- square brackets are used 
df["Bonus"] = df["Salary"] *0.1
print(df)

#syntax 2:- using insert method,we can give new column a desired position too  :- df.insert(location,"col_name",same_data)
df.insert(4,"Increment",df["Salary"]*0.2)
print(df)

"""--------------------UPDATING VALUES-----------------------------------------------"""
#df.loc[row_index,"col_name"] = new_values
df.loc[1,"score"] = 100
print(df.iloc[1]) #this print row 1
print(df)
df["Salary"] = df["Salary"]*1.05 #increased salary by 5%

"""--------------------DROPING COLUMN(THIS DELETES COLUMN)----------------------------"""
#df.drop(columns = ["Col_name"],inplace = True) , implace = true means modification happens in original dataset, false means new datset will be created
df.drop(columns=["Increment"],inplace=True)
print(df)
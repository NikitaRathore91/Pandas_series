import pandas as pd 

#reading csv file 
#df = pd.read_csv("sales_data_sample.csv",encoding ="latin1")
#df = pd.read_excel("FSI-2023-DOWNLOAD.xlsx",engine="openpyxl")
df = pd.read_json("sample_Data.json")
#print(df)

"""now creating a dataframe using dictionary """

data = {
    "Name" : ['Nikita','Ansh','Nikansh',],
    "Age" : [22,21,0],
    "city" : ['Khirkiya','delhi','Uterus']
} 
#print(data) : this will print in normal dictionary format
df = pd.DataFrame(data)
print(df) #this will print in form of table

""" saving it as csv file"""
df.to_csv("family.csv",index=False) #this will create a csv file with name family.csv  & index = false will remove the index

"""Saving this as excel file"""
df.to_excel("E_family.xlsx",index=False)

"""Saving to .json file"""
df.to_json("j_family.json")

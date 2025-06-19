#sorting data
#df.sort_values( by="Col_name"True/false, inplace  = True)
#True->Ascending ,False->descending

import pandas as pd

data = {
    "Name" : ["Arun","Varun","Nishchay","Karan","Naman"],
    "Age" : [20,21,20,25,20],
    "Salary" : [30000,20000,25000,22000,40000]
}

df = pd.DataFrame(data)
# df.sort_values(by="Name", ascending=True,inplace=True)
# df.reset_index(drop=True,inplace=True)
# print("Sorted Names")
# print(df)
print(df)
df.sort_values(by=['Age', 'Name'], ascending=[True, True],inplace=True)    #Primary sort: Age in ascending order → 19, 20, 20, 21, 25, Secondary sort: Name in ascendoing order among same Ages """
print(df)
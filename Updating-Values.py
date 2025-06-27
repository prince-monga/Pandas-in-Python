import pandas as pd

data={
    "Name":['Prince','Riya','Karan','Anjali','Rahul','Sita','Ravi','Amit'],
    "Age":[18,20,24,31,45,53,60,70],
    "Salary":[30000,20000,43000,40000,54000,60000,48000,58000],
    "Performance":[5,6,7,8,9,10,4,3]
}
df = pd.DataFrame(data)
print(df)
# Adding a new column to the DataFrame
df.loc[1,'Salary']=50000
print(df)
#df["Salary"]=df['Salary']+df['Salary']*0.1
#print(df)
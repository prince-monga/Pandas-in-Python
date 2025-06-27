import pandas as pd

data={
    "Name":['Prince','Riya','Karan','Anjali','Rahul','Sita','Ravi','Amit'],
    "Age":[18,20,24,31,45,53,60,70],
    "Salary":[30000,20000,43000,40000,54000,60000,48000,58000],
    "Performance":[5,6,7,8,9,10,4,3]
}
df = pd.DataFrame(data)
print(df)
# Sorting the DataFrame by 'Age' in ascending order
df.sort_values(by="Age",ascending=False,inplace=True)
print("\nDataFrame sorted by 'Age' in ascending order:")
print(df)
#sorting the DataFarme by Name and Salary in descending order
df.sort_values(by=["Name","Salary"],ascending=[True,False],inplace=True)
print("\nDataFrame sorted by 'Name' and 'Salary' in descending order:")
print(df)

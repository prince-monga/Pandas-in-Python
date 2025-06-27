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
df["Bouns"]=df["Salary"]* 0.1

print("\nDataFrame after adding a new column:")
print(df)

#using the insert() method to add a new column at a specific position

df.insert(2,"Experience",[1,2,3,4,5,6,7,8])

print("\nDataFrame after inserting a new column at position 2:")
print(df)
import pandas as pd

data={
    "Name":['Prince','Riya',None,'Anjali','Rahul','Sita','Ravi','Amit'],
    "Age":[18,20,None,31,45,53,60,70],
    "Salary":[30000,20000,None,40000,54000,60000,48000,58000],
    "Performance":[5,6,None,8,9,10,4,3]
}
df = pd.DataFrame(data)
print(df)

df.dropna(inplace=True)  # Remove rows with any missing values
print("\nDataFrame after removing rows with missing values:")   
print(df)
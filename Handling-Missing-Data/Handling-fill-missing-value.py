import pandas as pd

data={
    "Name":['Prince','Riya',None,'Anjali','Rahul','Sita','Ravi','Amit'],
    "Age":[18,20,None,31,45,53,60,70],
    "Salary":[30000,20000,None,40000,54000,60000,48000,58000],
    "Performance":[5,6,None,8,9,10,4,3]
}
df = pd.DataFrame(data)
print(df)
# Handling missing data in a DataFrame

#df.fillna(0, inplace=True)  # Fill missing values with 0
#print("\nDataFrame after filling missing values with 0:")
#print(df)

# You can also fill with a specific value for each column
#df.fillna({ 'Name': 'Unknown', 'Age': 0, 'Salary': 0, 'Performance': 0}, inplace=True)
#print(df)

# You can also fill with the mean, median, or mode of the column
df['Age'].fillna(df['Age'].mean(),inplace=True)  # Fill missing Age with mean
df['Salary'].fillna(df['Salary'].mean(),inplace=True)  # Fill missing Salary with mean
df['Performance'].fillna(df['Performance'].mean(), inplace=True)  # Fill missing Performance with mean
df.fillna({ 'Name': 'Unknown'}, inplace=True)  # Fill missing Name with 'Unknown'
print("\nDataFrame after filling missing Age with mean:")
print(df)
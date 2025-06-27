import pandas as pd
'''
1- Select specfic columns from a DataFrame
2- filter rows
3- combine multiple conditions condition
In pandas-
1- Use square brackets to select specific columns from a DataFrame.
2- Use boolean indexing to filter rows based on a condition.

Selecting Columnn Give output-
1-A series object containing the values of the specified column.
2-dataFrame multiple columns
'''
data={
    "Name":['Prince','Riya','Karan','Anjali','Rahul','Sita','Ravi','Amit'],
    "Age":[18,20,24,31,45,53,60,70],
    "Salary":[30000,20000,43000,40000,54000,60000,48000,58000],
    "Performance":[5,6,7,8,9,10,4,3]
}
df = pd.DataFrame(data)

Columnns=df[['Name','Age']]  # Selecting specific columns
print("Selected Columns:")  
print(Columnns)
one_column=df['Name']  # Selecting a single column
print("\nOne Column:")
print(one_column)


# Filtering rows based on a condition

filter_row=df[df['Age']>30]  # Filtering rows where Age is greater than 30
print("\nFiltered Rows (Age > 30):")
print(filter_row)


# Combining multiple conditions
Combine_multi=df[(df["Age"]>30) & (df["Salary"]>40000)]
print("\nFiltered Rows (Age > 30 and Salary > 40000):")
print(Combine_multi)

Combine_multi=df[(df["Age"]>30) | (df["Salary"]>40000)]
print("\nFiltered Rows (Age > 30 Or Salary > 40000):")
print(Combine_multi)
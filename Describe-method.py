#step 1 sample data frame

import pandas as pd

data={
    "Name":['Prince','Riya','Karan','Anjali','Rahul','Sita','Ravi','Amit'],
    "Age":[18,20,24,31,45,53,60,70],
    "Salary":[30000,20000,43000,40000,54000,60000,48000,58000],
    "Performance":[5,6,7,8,9,10,4,3]
}
df = pd.DataFrame(data)
# Display the DataFrame
print("Displaying the DataFrame:")
print(df)

#step 2 describe method
print("\nDescribing the DataFrame:")
print(df.describe())

'''
1- How to use the describe method in pandas?
The `describe()` method in pandas is used to generate descriptive statistics of a DataFrame. It
provides a summary of the central tendency, dispersion, and shape of the dataset's distribution, excluding `NaN` values. The output includes count, mean, standard deviation, minimum, maximum, and percentiles (25%, 50%, 75%) for each numeric column.

'''

'''
1-How big is your dataSet 
2- What are the names of the columns in your dataSet?
3- What is the data type of each column in your dataSet?
'''
print(f"Shape of the DataFrame: {df.shape}")
print(f"Columns in the DataFrame: {df.columns.tolist()}")

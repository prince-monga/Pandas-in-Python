#Read Row in pandas
import pandas as pd

#Use Head() and Tail() to read rows

df = pd.read_json('sample_Data.json', encoding='latin1')

#print("First 5 rows of the DataFrame:")
#print(df.head(10))  # Display the first 5 rows

print("\nLast 5 rows of the DataFrame:")
print(df.tail())  # Display the last 5 rows

'''
Vertical and horizontal concatenation of DataFrames using pandas.
# This code demonstrates how to concatenate DataFrames both vertically and horizontally using pandas.
'''

import pandas as pd

# Create two sample DataFrames
df1 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})                              

df2 = pd.DataFrame({
    "Name": ["David", "Eva", "Frank"],
    "Age": [28, 32, 40]
})

# Vertical concatenation (stacking DataFrames on top of each other)
df_Vertical=pd.concat([df1,df2],axis=0, ignore_index=True)    
print("Vertical Concatenation:")
print(df_Vertical)

# Horizontal concatenation (stacking DataFrames side by side)
df_Horizontal=pd.concat([df1,df2],axis=1, ignore_index=True)    
print("Horizontal Concatenation:")
print(df_Horizontal)
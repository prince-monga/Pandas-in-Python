import pandas as pd

data = {
    "Time":[1,2,3,4,5],
    "Value":[10,20,None,40,50]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Linear interpolation for missing values
df['Value']=df['Value'].interpolate(method='linear')
print("\nDataFrame after linear interpolation for missing values:")
print(df)
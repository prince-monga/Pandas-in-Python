import pandas as pd

df_Customer=pd.DataFrame({
    "CustomerID": [1, 2,4],
    "CustomerName": ["Prince", "Sinesh",  "Arun"]
})

df_order=pd.DataFrame({
    "OrderID": [101, 102, 103, 104],
    "CustomerID": [1, 2, 3, 4],
    "OrderAmount": [250.50, 150.75, 300.00, 200.00]
})

# Merging the two DataFrames on 'CustomerID'
df_merged=pd.merge(df_Customer, df_order, on="CustomerID", how="outer")
print("Merged DataFrame:")
print(df_merged)
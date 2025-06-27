import pandas as pd

data={
    "Name":['Prince','Riya','Karan'],
    "Age":[23,22,24],
    "City":['Delhi','Mumbai','Bangalore']
}
df=pd.DataFrame(data)
# Display the DataFrame
print(df)
# Save DataFrame to CSV
#df.to_csv('data.csv', index=False)

# Save DataFrame to XLSX
#df.to_excel('Output.xlsx', index=False)

# Save DataFrame to JSON
#df.to_json('data.json', orient='records', lines=True)

# Save DataFrame to HTML
df.to_html('data.html', index=False)

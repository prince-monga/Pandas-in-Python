import pandas as pd

#df =pd.read_json('sample_Data.json', encoding='latin1')
data={
    "Name":['Prince','Riya','Karan'],
    "Age":[23,22,24],
    "City":['Delhi','Mumbai','Bangalore']
}
df = pd.DataFrame(data)
print("Displaying the info of data set")
print(df.info())  # Display the info of the DataFrame
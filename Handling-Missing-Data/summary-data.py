import pandas as pd

#df =pd.read_json('sample_Data.json', encoding='latin1')
data={
    "Name":['Prince','Riya','Karan'],
    "Age":[23,22,24],
    "City":['Delhi','Mumbai','Bangalore'],
    "Salary":[30000,20000,43000],
}
df = pd.DataFrame(data)

avg_saalary=df["Salary"].mean() if "Salary" in df.columns else 0
print("Average Salary:", avg_saalary)
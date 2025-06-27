import pandas as pd

data={
    "Name":['Prince','Riya','Karan','Anjali','Rahul'],
    "Age":[23,22,24,22,23],
    "City":['Delhi','Mumbai','Bangalore','Chennai','Kolkata'],
    "Salary":[60000,20000,43000,70000,54000],
}
df = pd.DataFrame(data)
grouped= df.groupby("Age")["Salary"].mean()
print("Grouped Data by Age with Sum of Salary:")
print(grouped)

# multiple columns can be grouped
Grouped_multi=df.groupby(["Age","Name"])["Salary"].mean()
print("\nGrouped Data by Age and Name with Mean of Salary:")
print(Grouped_multi)
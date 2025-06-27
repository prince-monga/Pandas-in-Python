import pandas as pd 

#read the csv file
#df = pd.read_csv('sales_data_sample.csv',encoding='latin1')
#print(df)

#read json file
#df=pd.read_json('sample_Data.json', encoding='latin1')
#print(df)

#Read excel file
df = pd.read_excel('SampleSuperstore.xlsx')
print(df)
import pymongo

from bs4 import BeautifulSoup
import requests
from datetime import datetime
datetime_object = str(datetime.now()).replace(" ","").replace(".","").replace(":","")
dbname = 'covid-19-'+datetime_object
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-kwhwi.azure.mongodb.net/test?retryWrites=true&w=majority")

db = client.covid19

db.create_collection(dbname)

covid_col = db[dbname]

page = requests.get("https://www.worldometers.info/coronavirus/")


soup = BeautifulSoup(page.content,'html.parser')


table = soup.find_all('table')[0]

import pandas as pd

table_heads = table.find_all('th')
table_heads = [x.get_text() for x in table_heads]


table_rows = table.find_all('tr')

row_data = []
row_data_json = []
iterrows = iter(table_rows)
next(iterrows)
for row in iterrows:
    nl = []
    for data in row.find_all('td'):
        nl.append(data.get_text().strip())
    res = dict(zip(table_heads,nl))
    row_data.append(nl)
    row_data_json.append(res)

frame = pd.DataFrame(row_data,columns=table_heads)
frame.to_csv(dbname+'.csv')
frame.to_excel(dbname+'.xlsx')
frame.to_json(dbname+'.json')
print('created files')

covid_col.insert_many(row_data_json)
print(dbname + 'inserted into mongoDB')

# for row in row_data_json:
#     covid_col.insert_one(row)
#     print('inserted')



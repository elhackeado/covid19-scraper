from bs4 import BeautifulSoup
import requests
from datetime import datetime

datetime_object = str(datetime.now()).replace(" ","").replace(".","").replace(":","")

dbname = 'covid-19-2020-03-26180003250560'

msg = 'Task Completed at \t' + str(datetime.now()) + '\n' + 'CREATED ' + dbname+'.csv' + '\n' + 'CREATED ' + dbname+'.xlsx\n' + 'CREATED ' + dbname+'.json' + '\n' + 'INSERTED data into MongoDB in collection : ' + dbname + '\n' 
import slack
import nest_asyncio
nest_asyncio.apply()

channel = '#covid19-webscraper'

client = slack.WebClient(token='xoxp-1033025358789-1023046500033-1021622232467-4d46ca2a7015650f42b9b28839ea5434')

response = client.chat_postMessage(
    channel=channel,
    text=msg)
assert response["ok"]

response = client.files_upload(
    channels=channel,
    file=dbname+'.csv',
    title=dbname+'.csv')
assert response["ok"]


response = client.files_upload(
    channels=channel,
    file=dbname+'.xlsx',
    title=dbname+'.xlsx')
assert response["ok"]


response = client.files_upload(
    channels=channel,
    file=dbname+'.json',
    title=dbname+'.json')
assert response["ok"]



import requests, serial
from datetime import date
import time, calendar
from pySerialTransfer import pySerialTransfer as txfer

today = date.today()
formatted_date = today.strftime('/%Y/%#m/%#d')
local_date_day = int(today.strftime('%#d'))
local_date_month = int(today.strftime('%#m'))

#Seal Beach
id_1 = '739'
formatted_end = id_1 + formatted_date
response = requests.get('https://api.spitcast.com/api/spot_forecast/%s' % formatted_end)

forcast = response.json()
for i in forcast:
    if i['date_local']['dd'] == local_date_day and i['date_local']["mm"] == local_date_month and i['date_local']["hh"] == 8:
        surf_forcast = i
        break
size_ft = str(surf_forcast['size_ft'])[:4]
print(size_ft)
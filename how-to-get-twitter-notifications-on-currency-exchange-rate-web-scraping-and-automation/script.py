# https://towardsdatascience.com/how-to-get-twitter-notifications-on-currency-exchange-rate-web-scraping-and-automation-94a7eb240d60
# Parsing exchange rate based on target currency
# Use Slack instead of Twitter

import os
import time
from datetime import datetime
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup
from pytz import timezone

from slack import Slack

url = 'https://sg.finance.yahoo.com/currencies'
time_zone = 'Asia/Seoul'
target_currency = 'KRW'
file_name = 'usdto.txt'

html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

names=[]
prices=[]

for i in range(40, 572, 14): # all exchange rates
   for listing in soup.find_all('tr', attrs={'data-reactid':i}):
      for name in listing.find_all('td', attrs={'data-reactid':i+3}): # <td class="data-col0 Ta(start) Pstart(6px)" data-reactid="391"></td>
         names.append(name.text)
      for price in listing.find_all('td', attrs={'data-reactid':i+4}):
         prices.append(price.text)

currency=pd.DataFrame({"Names": names, "Prices": prices})
target_currency_price = currency[currency.Names.str.contains('USD/') & currency.Names.str.contains(target_currency)].Prices.item() # price only

t_zone = datetime.now(timezone(time_zone))
path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(path, file_name), 'r+') as f:   
   last_target_currency_price = f.readline()
   
   if target_currency_price != last_target_currency_price:
      f.seek(0) # to overwrite existing price
      f.write(target_currency_price)
      message = '1 USD to {} = *{}* \n {} Time {} '.format(target_currency, target_currency_price, time_zone.split('/')[1], t_zone.strftime("%H:%M:%S %m-%d-%y"))
      # 1 USD to KRW = 1,136.1899 
      # Seoul Time 02:17:31 04-07-19
      slack = Slack()
      slack.send_notification(message)


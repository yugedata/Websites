import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import bs4 as bs
import sqlalchemy as sa
import time
import re
from datetime import datetime
import json
import sys
import os


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('pythontesting-02b1b8200372.json', scope)
client = gspread.authorize(creds)

# entire list of all tickers. each script
tickers = ["AAPL"]
def scrapeYahoo():
    index = 0
    for tick in tickers:
        counter = 0
        sheet = client.open("testing123").get_worksheet(index)
        rawhtml = requests.get(url="https://finance.yahoo.com/quote/"+tick+"/options?p=" + tick).content.decode()
        htmlsoup = bs.BeautifulSoup(rawhtml, "html.parser")
        callrows = htmlsoup.find('tbody', {'data-reactid' : '60'}).find_all("tr")
        putrows = htmlsoup.find('table', {'class': "puts W(100%) Pos(r) list-options"}).find('tbody').find_all("tr")
        putrows.reverse()
        for row in callrows:
            if 'in-the-money' in str(row)[:100] or counter > 4:
                continue
            strike = row.find('td', {'class': 'data-col2'}).getText()
            last = row.find('td', {'class': 'data-col3'}).getText()
            bid = row.find('td', {'class': 'data-col4'}).getText()
            ask = row.find('td', {'class': 'data-col5'}).getText()
            change = row.find('td', {'class': 'data-col6'}).getText()
            volume = row.find('td', {'class': 'data-col7'}).getText()
            interest = row.find('td', {'class': 'data-col8'}).getText()
            volatility = row.find('td', {'class': 'data-col9'}).getText()
            t = datetime.now()
            sheet.append_row([strike, last, bid, ask, change, volume, interest, volatility, t.strftime("%m/%d/%Y %H:%M:%S"), "call"])
            time.sleep(1)
            counter += 1

        counter = 0
        for row in putrows:
            if 'in-the-money' in str(row)[:100] or counter > 4:
                continue
            strike = row.find('td', {'class': 'data-col2'}).getText()
            last = row.find('td', {'class': 'data-col3'}).getText()
            bid = row.find('td', {'class': 'data-col4'}).getText()
            ask = row.find('td', {'class': 'data-col5'}).getText()
            change = row.find('td', {'class': 'data-col6'}).getText()
            volume = row.find('td', {'class': 'data-col7'}).getText()
            interest = row.find('td', {'class': 'data-col8'}).getText()
            volatility = row.find('td', {'class': 'data-col9'}).getText()
            t = datetime.now()
            sheet.append_row([strike, last, bid, ask, change, volume, interest, volatility, t.strftime("%m/%d/%Y %H:%M:%S"), "put"])
            time.sleep(1)
            counter += 1
        index += 1








scrapeYahoo()

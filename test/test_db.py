#!/usr/bin/env python3

import pandas as pd
import numpy as np
import pymysql
import configparser
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = configparser.ConfigParser()
config.read(os.path.join(ROOT_DIR,'config.ini'))

conn = pymysql.connect(host=config['DATABASE']['DB_HOST'],
                       port=int(config['DATABASE']['DB_PORT']),
                       user=config['DATABASE']['DB_USER'],
                       password=config['DATABASE']['DB_PASSWD'],
                       db=config['DATABASE']['DB_NAME'])

df = pd.read_sql('select * from raw_stock_index_daily limit 0,10', conn)

df = df[['date','open','high','low','close']]
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df.index.name = 'Date'
df.columns = ['Open','High','Low','Close']

def getChange(d):
    print(d)
    print(type(d),d.shape)
    print('-----')
    return d[0]

print(df.shape)
print(df.head(5))
df['PrevClose'] = df['Close'].rolling(window=3, axis='rows').apply(getChange)
print(df)

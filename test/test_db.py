#!/usr/bin/env python3

import pandas as pd
import pymysql
from .. import config

conn = pymysql.connect(host=config.DB_HOST,
                       port=config.DB_PORT,
                       user=config.DB_USER,
                       password=config.DB_PASSWD,
                       db=config.DB_NAME)

data = pd.read_sql('select * from raw_stock_index_daily limit 0,10;', conn)

print(data.head())

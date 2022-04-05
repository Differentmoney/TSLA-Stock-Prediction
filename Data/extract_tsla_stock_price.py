from pandas_datareader import data
import pandas as pd

sd = '2012-11-16'
ed = '2017-09-29'

tsla_data = data.DataReader('TSLA', 'yahoo', sd, ed)
tsla_data.to_csv('Data/tsla_stock_price.csv')
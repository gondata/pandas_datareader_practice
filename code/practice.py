from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

y_symbols = ['TSLA', 'AAPL', 'PLTR']
startdate = '2020-01-01'
enddate = '2021-01-01'

for i in y_symbols:
    pdr.get_data_yahoo(i, start=startdate, end=enddate)['Adj Close'].to_csv(i+".csv")
import pandas as pd 
import numpy as np
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yf

# get data
def get_data(stock, start, end):    
    stockData = yf.download(stock, start, end)    
    stockData = stockData['Close']
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix
    
stockList = ['PLTR', 'HOOD']
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=100)
meanReturns, covMatrix = get_data(stockList, startDate, endDate)

print("\nMean Returns")
print(meanReturns)

print("\nCovariant Matrix") 
print(covMatrix)

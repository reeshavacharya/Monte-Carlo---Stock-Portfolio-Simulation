import yfinance as yf

# get data
def get_data(stock, start, end):    
    stockData = yf.download(stock, start, end)    
    stockData = stockData['Close']
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix
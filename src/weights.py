import numpy as np 

# setting portfolio weights of the stocks

def portfolio_weight(meanReturns):
    weights = np.random.random(len(meanReturns))
    weights /= np.sum(weights)
    return weights
import numpy as np
from getData import meanReturns, covMatrix
from weights import weights
import matplotlib.pyplot as plt

# monte carlo method

# number of simulations
mc_sims = 100
T = 100 #time-frame in days
number_of_stocks = len(weights)

# array to retrieve information from
meanM = np.full(shape=(T, number_of_stocks), fill_value=meanReturns)

# array to store information from
portfolio_sims = np.full(shape=(T, mc_sims), fill_value=0.0) 


initial_portfolio = 1000

# monte carlo loops
for m in range(0, mc_sims): 
    # we will be assuming that the daily returns are distributed by a multivariate normal distribution 
    # refer to: https://ibb.co/qphxyMm
    Z= np.random.normal(size=(T, number_of_stocks))
    
    # cholesky decomposition used to determine lower triangular matrix
    L = np.linalg.cholesky(covMatrix)

    innerProduct = np.inner(L,Z)
    dailyReturns = meanM.T + innerProduct
    
    # accumulate portfolio daily returns
    portfolio_sims[:,m] = np.cumprod(np.inner(weights, dailyReturns.T)+1) * initial_portfolio

average_portfolio = portfolio_sims.mean(axis=1)

plt.plot(average_portfolio, label="Average Portfolio Value")
plt.ylabel('Portfolio Vlaue ($)')
plt.xlabel('Days')
plt.title('Monte Carlo simulation of a stock portfolio (Average)')
plt.show()
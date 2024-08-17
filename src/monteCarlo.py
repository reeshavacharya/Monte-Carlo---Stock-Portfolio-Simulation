import numpy as np
from weights import portfolio_weight
import matplotlib.pyplot as plt

# monte carlo method

def monte_carlo(
    mean_returns,
    cov_matrix,
    number_of_simulations: int = 1000,
    days: int = 100,
    initial_portfolio_value: int = 1000
):
    weights = portfolio_weight(mean_returns)
    number_of_stocks = len(weights)
    
    # array to retrieve information from
    meanM = np.full(shape=(days, number_of_stocks), fill_value=mean_returns)
    
    # array to store information in
    portfolio_sims = np.full(shape=(days, number_of_simulations), fill_value=0.0)
    
    for m in range(0, number_of_simulations):
        # we will be assuming that the daily returns are distributed by a multivariate normal distribution 
        # refer to: https://ibb.co/qphxyMm
        Z= np.random.normal(size=(days, number_of_stocks))
        
        # cholesky decomposition used to determine lower triangular matrix
        L = np.linalg.cholesky(cov_matrix)

        inner_product = np.inner(L,Z)
        daily_returns = meanM.T + inner_product
        
        # accumulate portfolio daily returns
        portfolio_sims[:,m] = np.cumprod(np.inner(weights, daily_returns.T)+1) * initial_portfolio_value
    
    average_portfolio = portfolio_sims.mean(axis=1)

    # Plot all simulations
    plt.figure(figsize=(12, 6))
    plt.plot(portfolio_sims)  # Plot all simulations with some transparency
    plt.title('Monte Carlo Simulations of Portfolio Value')
    plt.ylabel('Portfolio Value ($)')
    plt.xlabel('Days')
    plt.show()
    
    # Plot average portfolio value
    plt.figure(figsize=(12, 6))
    plt.plot(average_portfolio)
    plt.title('Average Portfolio Value Over Simulations')
    plt.ylabel('Portfolio Value ($)')
    plt.xlabel('Days')
    plt.legend()
    plt.show()
    
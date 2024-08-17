from getData import get_data
from monteCarlo import monte_carlo

def simulate(stocks, startDate, endDate, number_of_simulations: int = 1000, days: int = 100, initial_portfolio_value: int = 1000): 
    mean_returns, cov_matrix = get_data(stocks, startDate, endDate)
    monte_carlo(
        mean_returns=mean_returns, 
        cov_matrix=cov_matrix, 
        number_of_simulations=number_of_simulations, 
        days=days, 
        initial_portfolio_value= initial_portfolio_value 
    )
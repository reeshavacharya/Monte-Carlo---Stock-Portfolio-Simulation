import numpy as np 
from getData import meanReturns

# setting portfolio weights of the stocks
weights = np.random.random(len(meanReturns))
weights /= np.sum(weights)

print("\nWeights", weights)
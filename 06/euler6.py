import numpy as np

print(2*np.sum([np.sum([i*j for i in range(1,j)]) for j in range(1,101)]))
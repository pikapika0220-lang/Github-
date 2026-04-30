import numpy as np
def arange_square_matrix(n):
    return np.array([np.arange(i,n+i) for i in range(n)])

print(arange_square_matrix(4))
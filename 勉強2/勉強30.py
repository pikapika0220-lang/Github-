import numpy as np
def arange_square_matrix(n):
    result = []
    for i in range(n):
        result.append(np.arange(i,n+i))
    return np.array(result)
print(arange_square_matrix(5))
C = [[1]]
for i in range(100):
    C.append([1]+[0]*i+[1])
    for j in range(i):
        C[i+1][j+1] = C[i][j] + C[i][j+1]

import matplotlib.pyplot as plt
plt.plot(C[100])
plt.show()
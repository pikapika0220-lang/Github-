import numpy as np
a1 = np.array([0, 1, 2, 3, 4, 5]) # 1次元配列
a2 = a1.reshape(2,3)              # 2×3の2次元配列
a1[1] = 6
print(a2)
print(a2.ravel())

print(np.random.rand(3))
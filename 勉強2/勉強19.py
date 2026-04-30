word = 'supercalifragilisticexpialidocious'
height = [0]*26
for c in word: 
    height[ord(c) - ord('a')] += 1
print(height)

import matplotlib.pyplot as plt
plt.plot(height)
plt.show()
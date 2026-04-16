import pandas as pd
import numpy as np
df = pd.DataFrame({'name': ['田中', '鈴木', '佐藤'],'age':  [25, 30, 22]})
d2 = pd.DataFrame(np.random.rand(12).reshape(4,3), columns= ['c1','c2','c3'])
print(df)
print(d2)
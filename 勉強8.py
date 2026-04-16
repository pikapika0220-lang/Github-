import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

iris = pd.read_csv('iris.csv')

X_iris=iris[['petal_length', 'petal_width']].values

model = KMeans(n_clusters=3) # k-meansモデル
model.fit(X_iris) # モデルをデータに適合
y_km=model.predict(X_iris) # クラスタを予測

iris['cluster']=y_km
iris.plot.scatter(x='petal_length', y='petal_width', c='cluster', colormap='viridis')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv')

X = iris[['petal_length']].values
y = iris['petal_width'].values
plt.scatter(X,y)
plt.show()

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error

# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

model=LinearRegression() # 線形回帰モデル
model.fit(X_train,y_train) # モデルを訓練データに適合
y_predicted=model.predict(X_test) # テストデータで予測
print(mean_squared_error(y_test,y_predicted)) # 予測精度
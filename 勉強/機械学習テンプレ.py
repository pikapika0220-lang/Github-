# 1. ライブラリのインポート
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 2. データ読み込み
df = pd.read_csv('data.csv')

# 3. 特徴量とラベルに分ける
X = df['特徴量の列']
y = df['ラベルの列']

# 4. 訓練・テストに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 5. モデルを用意
model = LinearSVC()  # モデルの種類は目的によって変える

# 6. 学習
model.fit(X_train, y_train)

# 7. 予測
y_predicted = model.predict(X_test)

# 8. 評価
print(accuracy_score(y_test, y_predicted))
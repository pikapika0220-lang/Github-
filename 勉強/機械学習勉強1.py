from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


dataset = load_iris()
x = dataset.data
t = dataset.target

# 訓練用データセットとテスト用データセットへの分割
x_train, x_test, t_train, t_test = train_test_split(x, t, test_size=0.3, random_state=0)
# モデルの定義
reg_model = LinearRegression()#直線を引いて予測するモデル
# モデルの訓練
reg_model.fit(x_train, t_train)#実際に直線を予測
# 訓練後のパラメータ w
print(reg_model.coef_)#傾き
# 訓練後のバイアス b
print(reg_model.intercept_)#切片をもらう

# 精度の検証
print(reg_model.score(x_train, t_train))
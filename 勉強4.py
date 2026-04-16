import pandas as pd
iris_d = pd.read_csv('iris.csv')


print (iris_d.loc[1:5, ['sepal_length','species']])
print (iris_d[(iris_d['sepal_length'] > 7.0) & (iris_d['sepal_width'] < 3.0)])
print(iris_d.describe())
import pandas as pd
iris = pd.read_csv('iris.csv')
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = pd.read_csv('iris.csv')
iris2=iris[(iris['species']=='versicolor')|(iris['species']=='virginica')]
X_iris=iris2[['petal_length','petal_width']].values
y_iris=iris2['species'].values

X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=0.3, random_state=1, stratify=y_iris)
model = LogisticRegression(solver='lbfgs')

model.fit(X_train,y_train)
y_predicted=model.predict(X_test)
print (accuracy_score(y_test,y_predicted))


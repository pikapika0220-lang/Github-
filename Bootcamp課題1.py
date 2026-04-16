import pandas as pd
import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer #Tfiの追加
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC

# ここに追加
def tokenize(text):
    tagger = MeCab.Tagger()
    return ' '.join([line.split('\t')[0] for line in tagger.parse(text).split('\n') if line and line != 'EOS'])

df = pd.read_csv('bootcamp課題３＿各種データ - 学習用データ.csv')
df2 = pd.read_csv('bootcamp課題３＿各種データ - 検証用データ.csv')
# ここに追加
df['概要文'] = df['概要文'].apply(tokenize)
df2['概要文'] = df2['概要文'].apply(tokenize)

Vectorizer = TfidfVectorizer(max_features=50000, ngram_range=(1,2))
X_trian = Vectorizer.fit_transform(df['概要文'])
X_test = Vectorizer.transform(df2['概要文'])

y_trian = df['業界']
y_test = df2['業界']

model = LinearSVC(max_iter=1000)
model.fit(X_trian,y_trian) # モデルを訓練データに適合
y_predicted=model.predict(X_test) # テストデータで予測
print (accuracy_score(y_test,y_predicted))

description = input("概要文を入力してください: ")
description = tokenize(description)
description = Vectorizer.transform([description]) #transformで変換
#モデルで予測
d_predicted=model.predict(description) # テストデータで予測
print (d_predicted)

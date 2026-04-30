import pandas as pd #表形式のデータを扱うツール
import MeCab #日本語を単語に分割
from sklearn.feature_extraction.text import TfidfVectorizer #Tfi(文字列を数字に変換するツール)の追加
from sklearn.metrics import accuracy_score #正答率を計算するツール
from sklearn.svm import LinearSVC #数値からラベルを予測,LogisticRegressionより精度高いはず

# ここに追加
def tokenize(text):
#Mecabによって(単語\t品詞情報)にし、かつ改行,(東京\t名詞,,,)
    tagger = MeCab.Tagger() #解析エンジン=tagger
    return ' '.join([line.split('\t')[0] for line in tagger.parse(text).split('\n') if line and line != 'EOS']) #EOS(文末マーク),空文字除外
#単語ごとに区切って並べ直す,split[0]で手前の情報だけ取る,tagger.parse(text)は(単語\t品詞情報).split('\n')で1行につき1(単語+品詞)のセットにする
#.joinでバラバラの文字列を単語の間に''(空文字)を加えて繋げる

df = pd.read_csv('/Users/toyomasuhayate/Desktop/Bootcamp/python勉強2/Bootcamp/bootcamp課題3_各種データ - 学習用データ.csv') #表形式にまとめる
df2 = pd.read_csv('/Users/toyomasuhayate/Desktop/Bootcamp/python勉強2/Bootcamp/bootcamp課題3_各種データ - 検証用データ.csv')
# ここに追加
df['概要文'] = df['概要文'].apply(tokenize) #概要文の列を指定＋tokenizeを適用
df2['概要文'] = df2['概要文'].apply(tokenize)

Vectorizer = TfidfVectorizer(max_features=50000, ngram_range=(1,2)) #文章を数値へ、処理上限の単語＋2単語をひとまとめ
X_trian = Vectorizer.fit_transform(df['概要文']) #学習＋文字を数値化
X_test = Vectorizer.transform(df2['概要文'])

y_trian = df['業界']
y_test = df2['業界']

model = LinearSVC(max_iter=1000) #言語モデル＋上限
model.fit(X_trian,y_trian) # 概要文と業界の関係を見つけ出し、モデルでラベルを貼る(上書き)
y_predicted=model.predict(X_test) # テストデータで予測(modelにfitは含まれる)
print (accuracy_score(y_test,y_predicted))#答えと回答を照らし合わせる

description = input("概要文を入力してください: ")
description = tokenize(description)
description = Vectorizer.transform([description]) #transformで変換,数値に変換
#モデルで予測
d_predicted=model.predict(description) # テストデータで予測
print (d_predicted)

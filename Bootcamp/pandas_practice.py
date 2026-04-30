import pandas as pd

df = pd.read_csv('kobe_news.csv')
print(df['リスクスコア'].describe())
import requests
import pandas as pd
from openai import OpenAI

client = OpenAI(api_key='')

def risk_and_summary(title,body): #chatのcompletionsにアクセスし実行
    response = client.chat.completions.create( 
        model = 'gpt-3.5-turbo', #createのキーワード引数
        messages=[ #createのキーワード引数
            {'role':'user','content': f'''
以下の記事を読んで、リスクスコアと要約を教えてください。

タイトル: {title}
本文: {body}

リスクスコアは被害範囲・被害程度・社会的影響・死傷者や被害金額を元に1〜100点で判定してください。
以下の形式で返してください。
リスクスコア: XX
要約: XXXX
'''} #f文字列は{}に引数をを埋め込める
        ]
    )
    return response.choices[0].message.content #スコア、要約が一体となった文字列を返す

from bs4 import BeautifulSoup
url = 'https://www.kobe-np.co.jp/news/jiken/'
response = requests.get(url) # HTMLを取得
soup = BeautifulSoup(response.text, 'html.parser') #HTMLの文字列を取得し、解析

articles = soup.select('ul.article-list a')

urls = set() #重複の排除

data = []
for article in articles:
    url = article['href'] #hrefの属性を取り出す
    if ('/news/jiken/' in url or '/news/sagi/' in url or'/news/sogo/' in url) and url.endswith('.shtml'):
        if url.startswith('https://www.kobe-np.co.jp'):
            url = url.replace('https://www.kobe-np.co.jp','')
        urls.add(url)        
urls = list(urls)[:10] #新しい10件をとる

base_url = 'https://www.kobe-np.co.jp'
for url in urls:
    article_url = base_url + url #フルURLを作成
    response = requests.get(article_url)
    soup2 = BeautifulSoup(response.text, 'html.parser') #HTMLの文字列を取得し、解析
    article =soup2.find('div', class_ = 'article-body') #divかつclass=,,であるものを見つける
    title = soup2.find('h1', class_='caption').text
    date = soup2.find('time').text
    body = ''.join([p.text for p in article.find_all('p')]) #本文をすべてくっつける

    result = risk_and_summary(title, body)  # ← ここで呼び出す
    lines = result.split('\n') #AIの改行は\n
    risk_score = lines[0].replace('リスクスコア: ', '') #リストの一つ目
    summary = lines[1].replace('要約: ', '') #リストの2つ目
    
    data.append({
        'タイトル': title,
        'リスクスコア': risk_score,''
        '要約': summary, 
        '本文': body
        }) #appendを用いることで自動的にCSVの列名（ヘッダー）になる

df = pd.DataFrame(data) #frameにまとめる
df.to_csv('kobe_news.csv', index=False) #CSVに書き出す＋行番号を含めない
print('完了！')


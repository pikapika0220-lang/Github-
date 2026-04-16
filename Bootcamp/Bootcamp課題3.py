import requests

from bs4 import BeautifulSoup
url = 'https://www.kobe-np.co.jp/news/jiken/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.select('ul.article-list a')
for article in articles:
    url = article['href']
    print(url)
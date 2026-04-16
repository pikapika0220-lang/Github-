import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, "html.parser")

url = 'https://www.yahoo.co.jp/'
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup")) 
elems #github 確認用
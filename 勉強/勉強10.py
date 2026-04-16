import requests
from bs4 import BeautifulSoup

url = 'https://www.yomiuri.co.jp'
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

elems = soup.select('body > div.uni-home > div > main > div.home-l-main__primary > section.home-headline > div.home-headline__contents > div > div.hero > div.item > h3 > a')
print(elems[0].contents[0])
print(elems[0].attrs['href'])
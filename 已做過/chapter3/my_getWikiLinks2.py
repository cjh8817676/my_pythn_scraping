from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")


for link in bsObj.find('div',{'id':'bodyContent'}).find_all('a',href = re.compile('^(/wiki/)((?!:).)*$')):
	if 'href' in link.attrs:
		print(link.attrs['href'])


'''
維基網頁上有很多頁頭、頁尾、測攔與其他連結:
/wiki/Kevin_Bacon
/wiki/Golden_Globe_Award_for_Best_Actor_%E2%80%93_Television_Series_Musical_or_Comedy
眾多連結終分成兩種: 1.主題連結 2.其他連結

大部分主題連結(相對於其他連結)會有三個共同特徵
1.他們都在id為bodyContent的div當中
2.URL中沒有冒號
3.URL以/wiki/開頭
'''
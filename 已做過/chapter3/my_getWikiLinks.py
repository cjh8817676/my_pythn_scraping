from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")

#找HTML裡標籤為a的
#print(bsObj.find_all('a'))  

#在標籤a 且屬性為href的印出
for link in bsObj.find_all('a'):
	if 'href' in link.attrs:  
		print(link.attrs['href'])

#在維基百科裡面  標籤a且屬性href 代表有連結

'''
這個程式會把此網站所有的連結(包括你不想要的)都抓取
所以需要訂定一個規則--正規劃
'''
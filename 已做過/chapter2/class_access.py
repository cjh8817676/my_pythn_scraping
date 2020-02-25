from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
tags = bsObj.findAll(lambda tag: len(tag.attrs) == 0)
#tag.attrs 為標籤下的屬性個數
#print(bsObj.find(lambda tag: len(tag.attrs) == 2) 

for tag in tags:
	print(tag)

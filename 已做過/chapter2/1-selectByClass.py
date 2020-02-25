from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")#連結
bsObj = BeautifulSoup(html, "html.parser")#解析  建立物件

#find_all(tag, attributes, recursive, text, limit, keywords)
#find(tag, attributes, recursive, text, keywords) 2個都可以過濾HTML網頁以根據不同屬性招出所需的全部或單一標籤。


nameList = bsObj.findAll("span", {"class":"green"})#BeautifulSoup的其他用法，只抓取綠色屬性的文字，並 存於串列

'''
for name in nameList:
    print(name.get_text())
'''
print(bsObj.div.span)
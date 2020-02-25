from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

'''
隨機種子: 程式在匯入必要的函式庫後做的第一件事是以系統
目前時間產生隨機亂數。這可確保程式每次執行時都有新路徑
'''
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))#只讀取主題連結

links = getLinks("/wiki/Kevin_Bacon")

for link in links: 
    print(link["href"])

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

'''
從一個連結到另一個連結隨機爬網站
'''
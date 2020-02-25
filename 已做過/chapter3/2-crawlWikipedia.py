from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1)
        print(bsObj.find(id ="mw-content-text").findAll("p")[0]) #擷取標頭的第一段文字
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href']) #編輯連結(不一定會有)
    except AttributeError:
        print("This page is missing something! No worries though!")
    
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        print(link.attrs)
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:#防止找到重複的網頁，因為第一個主題連結可能是自己。
                #We have encountered a new page
                newPage = link.attrs['href']
                print("----------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)

#一開始執行就是從首頁開始
getLinks("") 

'''
從維基首頁，對著首頁的第一個主題連結，進去後，再從該網頁的第一個主題連結一直一直爬下去....
'''
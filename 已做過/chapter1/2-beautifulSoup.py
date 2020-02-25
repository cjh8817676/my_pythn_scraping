from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")#得知讀取html
bsObj = BeautifulSoup(html.read(), "html.parser")
#可以指定要讀取html的特定部分
print(bsObj.h1.get_text())

print(bsObj.div)

print(bsObj.head)


'''
只用urllib值能達到連線的功能
BeautifulSoup可以再解析html
'''
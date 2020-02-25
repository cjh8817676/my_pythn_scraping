from urllib.request import urlopen
from urllib.error import HTTPError
#from urllib.error import URLErrorError
from bs4 import BeautifulSoup
import sys
#連線可靠與例外處裡
#網路擷取最糟糕的是執行程序存到資料庫當中，然後發現擷取程序因為遇到資料格式錯誤而停止執行


#html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
#1-在伺服器上找不到這個網頁 ， 會回傳 404 Not Found， urlopen會拋出"HTTPError"的例外
#2-找不到伺服器 ， urlopen會拋出"URLError"的例外


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:  #拋出例外
        print(e)
        #回傳null、中斷、或執行B計畫
        return None
		
    try:
        bsObj = BeautifulSoup(html, "html.parser") #-伺服器不存在、html是個none物件，可能會拋出AttributeError
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/exercises/exercise12.html") #故意打錯網址
#title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
    
    
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

#allText = bsObj.findAll(id="text") #只放1個參數
allText = bsObj.findAll('',{'id':'text'}) 
#7、8行是相等的



print(allText[0].get_text())#只印出內容，較易閱讀
#.get_text()從文件中取出標籤且只回傳文字的Unicode字串。
#print(allText) #可直接印出整個html
#print(allText[0])
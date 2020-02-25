from urllib.request import urlopen
#Retrieve HTML string from the URL
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
print(html.read())
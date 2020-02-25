from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://tsundora.com/s_list/so/sword_art_online")
bsObj = BeautifulSoup(html, "html.parser")

for sibling in bsObj.find("div",{"id":"post_content"}).div.next_siblings:
    print(sibling) 
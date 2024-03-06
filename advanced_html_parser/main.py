from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://pythonscraping.com/pages/warandpeace.html")
parsed_html = BeautifulSoup(html.read(), "html.parser")

nameList = parsed_html.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())



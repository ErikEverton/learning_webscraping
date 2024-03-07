from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://trends.builtwith.com/websitelist/Responsive-Tables")
parsed_html = BeautifulSoup(html.read(), "html.parser")

for data in parsed_html.find('table', {"class": "table"}).tbody.tr:
    print(data.get_text())


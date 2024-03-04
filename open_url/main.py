from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.google.com/")
parsed_html = BeautifulSoup(html.read(), 'lxml')
print(parsed_html.prettify())

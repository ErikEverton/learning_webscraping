from urllib.request import urlopen

html = urlopen("https://www.google.com/")
print(html.read())

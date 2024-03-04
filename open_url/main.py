from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def get_link(parsed_html):
    try:
        title = parsed_html.body.a
    except AttributeError as error:
        return None
    return title


def main():
    try:
        html = urlopen("https://www.google.com/")
    except HTTPError as error:
        print(error)
    except URLError as error:
        print(error)
    else:
        parsed_html = BeautifulSoup(html.read(), 'lxml')
        link = get_link(parsed_html=parsed_html)
        if link:
            print(link)
        else:
            print("Title could not be found")

main()

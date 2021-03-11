import requests
from bs4 import BeautifulSoup


URL = 'https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0 Waterfox/78.7.0'
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def parse_products():
    html = get_html(URL)
    if html.status_code == 200:
        print(html.text)
    else:
        print('Error')


if __name__ == '__main__':
    parse_products()

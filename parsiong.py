import requests
from bs4 import BeautifulSoup

def get_url(url):
    result = requests.get(url)
    return result.text

def get_data(html, title):
    soup = BeautifulSoup(html, 'lxml')
    datas = soup.find_all('p')
    for data in datas:
        print('=---asd-sdasdasjkdhsauidfgsuyf')
        print(title)
        print('+++++++++++++++++++++++')
        print(data)
        print('===============')
        
def get_urls(url,title):
    urls = 'https:' + url
    result = requests.get(urls)
    get_data(result.text,title)

def get_datas(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('a', attrs={'class':'newslink'})
    for item in items:
        item_href = item.get('href')
        if 'sputnik' in item_href:
            get_urls(item_href,item.get_text())

def main():
    url = 'https://sputnik.kg/'
    total = get_url(url)
    get_datas(total)

main()
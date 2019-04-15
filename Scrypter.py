from celery import Celery, group, chord
from bs4 import BeautifulSoup
import requests
import json

app = Celery('bs2',broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

def fetch(url, num):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, features='html.parser')
    items = soup.find_all('a', class_ ='list__item__content__title__name')
    urls = [url['href'] for url in items]
    chord(group(product_detail.s(u, num) for u in urls))(result_print.s())

@app.task
def result_print(results): #ensure that i is equal to  range of iterations in 36th line
    print(json.dumps(results))


@app.task
def product_detail(url, num):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, features='html.parser')
    title = soup.find('h1').text.strip()
    photos = [p['href'] for p in soup.find_all('a', {'data-fancybox': 'photo'})]
    try:
        price = soup.find('div', class_ = 'ogl__details__desc').text
    except AttributeError:
        price = None
    return {'tytul':title,'zdjecia':photos,'cena':price, 'page num': num}

if __name__ == '__main__':
    for i in range(1, 4): #amount of pages
        fetch(f'https://ogloszenia.trojmiasto.pl/elektronika/?strona={i}', i) #enter url of the page you want to scrype

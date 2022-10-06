import requests
from bs4 import BeautifulSoup


def get_daily_horoscope(some_sign='libra', day='today'):
    response = requests.get(f"https://horo.mail.ru/prediction/{some_sign}/{day}/")
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    return soup.find('div', class_='article__text').text
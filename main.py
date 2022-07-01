import os
import requests
from urllib.parse import urlparse


def is_bitlink(bitly_token, url):
    parsed_url = urlparse(user_url)
    netloc, path = parsed_url.netloc, parsed_url.path
    headers = {
        'Authorization': f'Bearer {bitly_token}',
    }
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{netloc}{path}',
        headers=headers
    )
    return response.ok


def get_bitlink(bitly_token, url):
    headers = {
        'Authorization': f'Bearer {bitly_token}',
    }
    data = {"long_url": url}
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json=data
    )
    response.raise_for_status()
    return response.json()['link']


def count_clicks(bitly_token, url):
    parsed_url = urlparse(user_url)
    netloc, path = parsed_url.netloc, parsed_url.path    
    headers = {
        'Authorization': f'Bearer {bitly_token}',
    }
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{netloc}{path}/clicks/summary',
        headers=headers,
    )
    response.raise_for_status()
    return response.json()['total_clicks']


if __name__ == '__main__':
    bitly_token = os.environ['BITLY_TOKEN']
    user_url = input('Введите ссылку \n')
    try:
        if is_bitlink(bitly_token, user_url):
            print('По ссылке перешли:',
                  count_clicks(bitly_token, user_url),
                  'раз(а)')
        else:
            print('Битлинк', get_bitlink(bitly_token, user_url))
    except requests.exceptions.HTTPError:
        print('404. Страница не найдена')
    except requests.exceptions.MissingSchema:
        print('Введите корректную ссыллку.(Пример: https://www.google.com/)')

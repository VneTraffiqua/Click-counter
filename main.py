from dotenv import load_dotenv
import requests
import argparse
import os
from urllib.parse import urlparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('user_url', nargs='?')
    return parser.parse_args()


def is_bitlink(service_token, url):
    parsed_url = urlparse(url)
    netloc, path = parsed_url.netloc, parsed_url.path
    headers = {
        'Authorization': f'Bearer {service_token}',
    }
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{netloc}{path}',
        headers=headers
    )
    return response.ok


def get_bitlink(service_token, url):
    headers = {
        'Authorization': f'Bearer {service_token}',
    }
    data = {"long_url": url}
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json=data
    )
    response.raise_for_status()
    return response.json()['link']


def count_clicks(service_token, url):
    parsed_url = urlparse(url)
    netloc, path = parsed_url.netloc, parsed_url.path    
    headers = {
        'Authorization': f'Bearer {service_token}',
    }
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{netloc}{path}/clicks/summary',
        headers=headers,
    )
    response.raise_for_status()
    return response.json()['total_clicks']


if __name__ == '__main__':
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')
    user_url = get_args().user_url
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

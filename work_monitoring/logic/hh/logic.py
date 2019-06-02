# https://github.com/hhru/api

import requests

BASE_URL = 'https://api.hh.ru/'
CONNECT_TIMEOUT = 60
READ_TIMEOUT = 60


def get_search_vacancies(text=None):
    url = '{}vacancies?text={}&area=1&from=cluster_area'.format(BASE_URL, text)
    try:
        r = requests.get(url, timeout=(CONNECT_TIMEOUT, READ_TIMEOUT))
    except requests.exceptions.ReadTimeout:
        raise Exception('Истек таймаут чтения')
    except requests.exceptions.ConnectTimeout:
        raise Exception('Истекло время ожидания соединения c сервером')
    except requests.exceptions.ConnectionError:
        raise Exception('Неудалось подключится к серверу')
    except requests.exceptions.HTTPError as err:
        raise Exception('Произошла ошибка HTTP: {}'.format(err.response.content))

    try:
        data = r.json()
    except Exception as arr:
        raise Exception(arr)

    return data


def get_count_search_vacancies(text=None):
    data = get_search_vacancies(text)
    if isinstance(data, dict):
        return data.get('found')
    else:
        raise Exception('Полученные данные не являются словарем')


print(get_count_search_vacancies('python'))

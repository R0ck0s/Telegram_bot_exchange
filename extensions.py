import requests
import json
from config import keys, API_KEY

class APIException(Exception):
    pass

class Converter:

    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f" https://currate.ru/api/?get=rates&pairs={keys[base]}{keys[quote]}&key={API_KEY}")
        total_base = json.loads(r.content)['data'][f'{keys[base]}{keys[quote]}']

        return total_base

import requests


def get_tickets(url_req):
    result = requests.get(url_req)
    return result.json()


def get_available_tickets(lib, count_tickets_in_line):
    lib_keys = list(lib.keys())
    result = ''
    while len(lib_keys) > count_tickets_in_line:
        result += ', '.join(lib_keys[:count_tickets_in_line]) + '\n'
        for keys in lib_keys[:count_tickets_in_line]:
            lib_keys.remove(keys)
    result += ', '.join(lib_keys)
    return result


def choose_ticket(message, lib):
    count_try = 0
    ticket = input(message).strip()
    while count_try <= 9:
        if ticket in lib:
            return ticket
        else:
            ticket = input('Указанная валюта не найдена, попробуйте еще раз: ').strip()
        count_try += 1
    print('My job here is done!')
    exit('Превышено количество попыток ввода')


def entering_number(message, count_round):
    count_try = 0
    number = input(message).strip()
    while count_try < 9:
        try:
            result = round(float(number), count_round)
            return result
        except:
            number = input('Введеное значение должно быть числом, попробуйте еще раз: ').strip()
        count_try += 1
    print('My job here is done!')
    exit('Превышено количество попыток ввода')


def convert_ticket(from_currency, to_currency, amount_currency, lib):
    convert_coefficient = lib[to_currency] / lib[from_currency]
    result = amount_currency * convert_coefficient
    return result


URL = 'https://api.freecurrencyapi.com/v1/latest?apikey='
URL_PARAMS = 'currencies='
API_KEY = 'fca_live_mvzs5GSll5nO70RxrnU3L2TOE1DYOoxfcYoMG4tD'

tickets_lib = get_tickets(f'{URL}{API_KEY}&{URL_PARAMS}')['data']

print(f'''Конвертер валют

Для работы с программой потребуется:
- Выбрать исходную валюту
- Выбрать конечную валюту
- Ввести количество исходной валюты

Доступные валюты:''')

print(get_available_tickets(tickets_lib, 10))
print()

from_ticket = choose_ticket('Введите исходную валюту: ', tickets_lib)
to_ticket = choose_ticket('Введите конечную валюту: ', tickets_lib)
amount = entering_number('Введите количество исходной валюты: ', 2)

converted_amount = round(convert_ticket(from_ticket, to_ticket, amount, tickets_lib), 2)

print()
print(f'Результат: {amount} {from_ticket} = {converted_amount} {to_ticket}')

import requests

URL = 'https://api.freecurrencyapi.com/v1/latest?apikey='
URL_PARAMS = 'currencies='
API_KEY = 'fca_live_mvzs5GSll5nO70RxrnU3L2TOE1DYOoxfcYoMG4tD'


def get_ticket(url_req):
    result = requests.get(url_req)
    return result.json()


def print_available_ticket(lib, count_tickets_in_line):
    count = 0
    result = ''
    for ticket in lib:
        if result == '':
            result = ticket
        else:
            result += ', ' + ticket
        count += 1
        if count >= count_tickets_in_line:
            print(result)
            count = 0
            result = ''
    if result != '':
        print(result)


def choose_ticket(message, lib):
    count_try = 0
    ticket = input(message).strip()
    while count_try <= 10:
        if ticket in lib:
            return ticket
        else:
            ticket = input('Указанная валюта не найдена, попробуйте еще раз: ').strip()
        count_try += 1
    print('My job here is done!')
    exit('Превышено количество попыток ввода')


def convert_ticket(from_currency, to_currency, amount_currency, lib):
    convert_coefficient = lib[to_currency] / lib[from_currency]
    result = amount_currency * convert_coefficient
    return result


tickets_lib = get_ticket(f'{URL}{API_KEY}&{URL_PARAMS}')['data']

print(f'''Конвертер валют

Для работы с программой потребуется:
- Выбрать исходную валюту
- Выбрать конечную валюту
- Ввести количество исходной валюты

Доступные валюты:''')

print_available_ticket(tickets_lib, 10)
print()

from_ticket = choose_ticket('Введите исходную валюту: ', tickets_lib)
to_ticket = choose_ticket('Введите конечную валюту: ', tickets_lib)
amount = float(input('Введите количество исходной валюты: ').strip())

converted_amount = round(convert_ticket(from_ticket, to_ticket, amount, tickets_lib), 2)

print()
print(f'Результат: {amount} {from_ticket} = {converted_amount} {to_ticket}')
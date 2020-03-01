"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""
import re


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def validator(string):
    match_1 = re.fullmatch(r'[-+]?\d+', string)
    match_2 = re.fullmatch(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', string)
    if match_1:
        return string, 'int'
    elif match_2:
        return string, 'float'
    else:
        raise OwnError("Необходимо вводить только числа!")


my_list = []
while True:
    n = input('Введите число или введите "stop" чтобы остановить ввод: ')
    try:
        if n != 'stop':
            val = validator(n)
        else: break
        if val[1] == 'int':
            my_list.append(int(n))
        elif val[1] == 'float':
            my_list.append(float(n))
    except OwnError as err:
        print(err)
print(my_list)

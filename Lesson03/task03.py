"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    """
    Возвращает сумму двух наибольших параметров

    :param a:
    :param b:
    :param c:
    :return:
    """
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    return sum(my_list)


try:
    args = []
    for i in range(3):
        args.append(int(input(f'Введите аргумент {i + 1}: ')))
    print(f'Сумма двух наибольших аргументов = {my_func(args[0], args[1], args[2])}')
except ValueError:
    print('Аргументы должны быть числовыми')

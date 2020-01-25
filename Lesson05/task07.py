"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее ​не включать.​
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""
import json


def check_digits(s):
    """
    Проверяем на цифры в строке, если цифровая, то преобразуем в int

    :param s:
    :return:
    """
    s = str(s)
    if s.isdigit():
        return int(s)
    return s


def av_profit(dict):
    """
    Расчёт средней прибыли

    :param dict:
    :return:
    """
    sum_prof = 0
    for k, v in dict.items():
        sum_prof += v
    return round(sum_prof / len(dict), 2)


try:
    firm_list = []  # инициализируем список фирм
    with open('task07_input.txt', 'r', encoding='utf8') as f_in:            # считываем фирмы из файла и добавляем в список
        for line in f_in:
            firm_list.append(tuple(map(check_digits, line.split())))
    firm_dict = {firm[0]: (firm[2] - firm[3]) for firm in firm_list}        # формируем словарь из списка фирм
    profit_dict = {k: v for k, v in firm_dict.items() if v >= 0}            # прибыльные фирмы
    result_list = [firm_dict, {'average_profit': av_profit(profit_dict)}]   # итоговый словарь для записи в файл
    with open('task07_out.json', 'w', encoding='utf8') as f_out:
        json.dump(result_list, f_out, indent=4)
except IOError:
    print('Произошла ошибка ввода-вывода!')

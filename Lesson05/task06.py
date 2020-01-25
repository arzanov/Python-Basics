"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.

"""

my_list = []
my_dict = {}
try:
    with open('task06_input.txt', 'r', encoding='utf8') as f:
        for line in f:
            my_list.append(tuple(map(str, line.split())))
    for i in my_list:
        sum_lessons = 0
        for j in i[1:]:
            if j != '-':
                sum_lessons += int(j[:j.index('(')])
        my_dict.update({i[0]: sum_lessons})
    print(my_dict)
except IOError:
    print('Произошла ошибка ввода-вывода!')

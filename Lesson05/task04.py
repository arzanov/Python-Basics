"""
Создать (не программно) текстовый файл со следующим содержимым:
One - 1
Two - 2
Three - 3
Four - 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
"""


def rus_dict(key):
    r_dict = {'1': 'Один',
              '2': 'Два',
              '3': 'Три',
              '4': 'Четыре'}
    return r_dict[key]


try:
    f_in = open('file_in.txt', 'r', encoding='utf8')
    f_out = open('file_out.txt', 'w', encoding='utf8')

    for line in f_in:
        l_list = list(map(str, line.split()))
        l_list[0] = rus_dict(l_list[2])
        print(' '.join(l_list), file=f_out)

    f_in.close()
    f_out.close()
except IOError:
    print('Произошла ошибка ввода-вывода!')

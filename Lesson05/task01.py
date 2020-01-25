"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

"""


def check_file_name(file_name):
    try:
        f = open(file_name, 'w', encoding='utf8')
        f.close()
        return True
    except FileNotFoundError:
        print('Недопустимое имя файла. Попробуйте снова.')
    except IOError:
        print('Произошла ошибка ввода-вывода!')
    return False


def write_to_file(file_name, info):
    try:
        with open(file_name, 'w', encoding='utf8') as f:
            for i in range(len(info)):
                print(info[i], file=f)
    except IOError:
        print('Произошла ошибка ввода-вывода!')


def user_input(input_list):
    while True:
        i = input()
        if i != '':
            input_list.append(i)
        else:
            break


while True:
    f_n = input('Как назовем файл? (Только имя, без расширения) : ') + '.txt'
    if check_file_name(f_n):
        break
my_list = []
user_input(my_list)
write_to_file(f_n, my_list)

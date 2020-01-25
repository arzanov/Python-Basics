"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.

"""

try:
    with open('file.txt', 'w', encoding='utf8') as f:
        print(*list(map(int, input().split())), file=f)

    with open('file.txt', 'r', encoding='utf8') as f:
        print(f'Сумма чисел в файле : {sum(list(map(int, f.read().split())))}')
except IOError:
    print('Произошла ошибка ввода-вывода!')

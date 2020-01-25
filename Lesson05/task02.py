"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.

"""

words = 0
lines = 0
try:
    with open('file.txt', 'r', encoding='utf8') as f:
        for line in f:
            lines += 1
            words += len(line.split())
        print(f'File {f.name} contents {words} words in {lines} lines',)
except IOError:
    print('Произошла ошибка ввода-вывода!')

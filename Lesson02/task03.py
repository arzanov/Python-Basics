# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('Введите номер месяца от 1 до 12: '))

# решение через list
winter = (1, 2, 12)
spring = (3, 4, 5)
summer = (6, 7, 8)
autumn = (9, 10, 11)
if month in winter:
    print('Зима')
elif month in spring:
    print('Весна')
elif month in summer:
    print('Лето')
elif month in autumn:
    print('Осень')
else:
    print('Месяца с таким номером не существует')

# решение через dict
year = {'Зима': (1, 2, 12),
        'Весна': (3, 4, 5),
        'Лето': (6, 7, 8),
        'Осень': (9, 10, 11)}
print(*[year_time for (year_time, m_number) in year.items() if month in m_number])

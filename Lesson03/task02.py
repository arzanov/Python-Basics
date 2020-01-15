"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
    имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

"""


def big_data(name, surname, year, city, email, phone):
    data = {'Name': name,
            'Surname': surname,
            'Year': year,
            'City': city,
            'Email': email,
            'Phone': phone}
    return data


print('Введите данные пользователя')
n = input('Имя: ')
s = input('Фамилия: ')
y = input('Год рождения: ')
c = input('Город проживания: ')
e = input('Email: ')
p = input('Телефон: ')
print(big_data(name=n, surname=s, year=y, city=c, email=e, phone=p))

"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import re


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyDate:
    def __init__(self, string):
        self.string = string
        self.digit = self.date_to_digit(self.string)
        self.day = self.digit[0]
        self.month = self.digit[1]
        self.year = self.digit[2]

    @staticmethod
    def validator(string):
        match = re.fullmatch(r'^[0-3][0-9]-[0|1][0-9]-(19|20)[0-9]{2}', string)
        if match:
            return string
        else:
            raise OwnError("Неверный формат даты. Необходимо DD-MM-YYYY")

    @classmethod
    def date_to_digit(cls, string):
        try:
            string = MyDate.validator(string)
            date_list = string.split('-')
            for i in range(len(date_list)):
                date_list[i] = int(date_list[i])
            return tuple(date_list)
        except OwnError as err:
            print(err)


md = MyDate('14-10-2020')   # Создание обычного экземпляра класса
print(md.digit)             # Дата в цифровом формате
print(MyDate.date_to_digit('25-12-2000'))   # Вызов метода класса

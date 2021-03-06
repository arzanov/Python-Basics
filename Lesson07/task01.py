"""
Реализовать класс ​Matrix (​матрица). Обеспечить перегрузку конструктора класса (метод __init__())​,
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — ​система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода ​__str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода ​__add__()
для реализации операции сложения двух объектов класса ​Matrix (​двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, in_list):
        self.matrix = in_list

    def __str__(self):
        my_str = ''
        for line in self.matrix:
            for el in line:
                my_str += f'{str(el)}\t'
            my_str += '\n'
        return my_str

    def __add__(self, other):
        result = []
        for y in range(len(self.matrix)):
            line = []
            for x in range(len(self.matrix[y])):
                line.append(self.matrix[y][x] + other.matrix[y][x])
            result.append(line)
        return Matrix(result)


m1 = Matrix([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
m2 = Matrix([[11, 12, 13],
             [14, 15, 16],
             [17, 18, 19]])
print(m1 + m2)

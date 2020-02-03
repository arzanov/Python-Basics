"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
                                 и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNum:
    def __init__(self, my_str):
        self.my_str = my_str
        self.real, self.im = self.str_to_num(self.my_str)

    def str_to_num(self, my_str):
        my_list = my_str.split()
        self.real = float(my_list[0])
        self.im = float(my_list[2][:-1]) if my_list[1] == '+' else -float(my_list[2][:-1])
        return self.real, self.im

    def __add__(self, other):
        res_real = self.real + other.real
        res_im = self.im + other.im
        im_sign = '+' if res_im >= 0 else '-'
        res_str = f'{str(res_real)} {im_sign} {str(abs(res_im))}i'
        return res_str

    def __mul__(self, other):
        res_real = self.real * other.real + (self.im * other.im) * (-1)
        res_im = self.real * other.im + self.im * other.real
        im_sign = '+' if res_im >= 0 else '-'
        res_str = f'{str(res_real)} {im_sign} {str(abs(res_im))}i'
        return res_str


num_1 = ComplexNum('10 - 15i')
num_2 = ComplexNum('15 + 10i')
print(num_1 + num_2)
print(num_1 * num_2)

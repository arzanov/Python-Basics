# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print('Сумма чисел равна ', a + b, f', а их отношение равно {(a / b):.2f}')
c = str(a) + str(b)
print('Также эти числа образуют собой число ', c)
if int(c) % 2 == 0:
    print('которое является четным.')
else:
    print('которое является нечетным.')
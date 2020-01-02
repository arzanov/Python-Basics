# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


my_list = list(map(int, input('Введите элементы списка через пробел: ').split()))
if len(my_list) > 1:
    print(f'Исходный список : \t{my_list}')
    new_list = []
    for i in range(0, len(my_list), 2):
        new_list.extend(reversed(my_list[i:i+2]))
    print(f'Новый список : \t\t{new_list}')
else:
    print('Здесь нечего обменивать. Список слишком короткий.')
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


time_s = int(input('Введите время в секундах: '))
s = time_s % 60                             # считаем секунды
m = (time_s // 60) % 60                     # считаем минуты
h = time_s // 3600                          # считаем часы
print(f'Это соответствует: {h:02d}:{m:02d}:{s:02d}')

"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т

"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight(self):
        global weight_of_sq_sm, thickness
        weight = self._length * self._width * weight_of_sq_sm * thickness / 1000
        return weight


weight_of_sq_sm = 25    # Вес квадратного сантиметра асфальта в кг
thickness = 5           # Тощина дорожного полотна в см
road_1 = Road(5000, 20)
print(f'На дорогу длинной {road_1._length}м и '
      f'шириной {road_1._width}м потребуется {road_1.get_weight()} тонн асфальта.')

"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""


class Car:
    def __init__(self, speed, color, name, is_police):
        """
        Базовый класс для определения автомобиля

        :param speed: скорость
        :param color: цвет
        :param name: наименование
        :param is_police: True or False
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} машина поехала')

    def stop(self):
        print(f'{self.name} машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')
        if self.speed > 60:
            print('Внимание! Скорость превышена!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')
        if self.speed > 40:
            print('Внимание! Скорость превышена!')


class PoliceCar(Car):
    pass


cars = [TownCar(75, 'black', 'Городская', False),
        SportCar(120, 'red', 'Спортивная', False),
        WorkCar(50, 'yellow', 'Рабочая', False),
        PoliceCar(80, 'white', 'Полицейская', True)]
print('Созданы автомобили:\n')
for c in cars:
    print(f'{c.name}\tцвет: {c.color}\t{"(полиция)" if c.is_police else ""}')
print()
cars[0].go()
cars[1].turn('налево')
cars[2].stop()
print('\nПроверка скорости:')
for c in cars:
    print(f'{c.name} :\t', end='')
    c.show_speed()
    print()

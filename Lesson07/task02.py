"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — ​одежда,​ которая может иметь определенное название.
К типам одежды в этом проекте относятся ​пальто ​и ​костюм.
​У этих типов одежды существуют параметры:
​размер (​для ​пальто)​​и ​рост (​для ​костюма)​. Это могут быть обычные числа: ​V и H,​соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
​для костюма (​2*H + 0.3).
​Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора ​@property.​
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def textile_calc(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        super().__init__(size)
        self.v = size

    @property
    def textile_calc(self):
        return round(self.v / 6.5 + 0.5, 2)


class Suite(Clothes):
    def __init__(self, size):
        super().__init__(size)
        self.h = size

    @property
    def textile_calc(self):
        return round(2 * self.h + 0.3, 2)


coat_1 = Coat(48)
suite_1 = Suite(4)
print(f'Для пошива костюма {suite_1.h} роста требуется {suite_1.textile_calc} кв.м ткани')
print(f'Для пошива пальто размером {coat_1.v} требуется {coat_1.textile_calc} кв.м ткани')

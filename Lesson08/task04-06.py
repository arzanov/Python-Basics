"""
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""
import inspect


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.equip = {}

    def add_equipment(self, equip, quantity=1):
        if equip in self.equip:
            self.equip[equip] += quantity
        else:
            self.equip.update({equip: quantity})
        if inspect.stack()[1][3] == '<module>':
            print(f'{quantity} pieces of {equip.short_print} added to {self.name}')

    def move_equipment(self, other, equip, quantity=1):
        if equip in self.equip:
            if self.equip[equip] >= quantity:
                self.equip[equip] -= quantity
                other.add_equipment(equip, quantity)
                print(f'{quantity} pieces of {equip.short_print} moved to {other.name}')
            else:
                print(f'No needed quantity on {self.name}')
        else:
            print(f'No this equipment on {self.name}')

    def list_equipment(self):
        print(f'{self.name} contents:')
        print(f'\tID\t\t\tEquipment\t\t\t\t\t\tQuantity')
        for k, v in self.equip.items():
            print(f'{k}\t\t\t\t{v}')


class Equipment:
    id = 0

    def __init__(self, vendor, model):
        Equipment.id += 1
        self.id = Equipment.id
        self.vendor = vendor
        self.model = model

    def __str__(self):
        return f'\t{self.id}\t{self.__class__.__name__}\t{self.vendor} {self.model}'

    @property
    def short_print(self):
        return f'{self.__class__.__name__}\t{self.vendor} {self.model}'


class Printer(Equipment):
    def __init__(self, vendor, model, print_speed):
        super().__init__(vendor, model)
        self.print_speed = print_speed

    def __str__(self):
        return f'\t{self.id}\t{self.__class__.__name__}\t{self.vendor} {self.model}'


class Scanner(Equipment):
    def __init__(self, vendor, model, scan_res):
        super().__init__(vendor, model)
        self.scan_res = scan_res


class Copier(Equipment):
    def __init__(self, vendor, model, copy_speed):
        super().__init__(vendor, model)
        self.copy_speed = copy_speed


# Инициализируем склады
warehouses = [Warehouse('Main store'),
              Warehouse('Accounting'),
              Warehouse('HR'),
              Warehouse('IT')]
# Создаём базу оборудования
equipment = [Printer('HP', 'OfficeJet 355 FDN', '100ppm'),
             Scanner('Epson', 'HomeScan  Plus', '3200ppi'),
             Copier('Xerox', 'WorkCentre 751', '200ppm')]
# Добавляем оборудование на главный склад
warehouses[0].add_equipment(equipment[0], 20)
warehouses[0].add_equipment(equipment[1], 15)
warehouses[0].add_equipment(equipment[2], 10)
# Переносим оборудование в отделы
# Бухгалтения
warehouses[0].move_equipment(warehouses[1], equipment[0], 4)
warehouses[0].move_equipment(warehouses[1], equipment[1], 3)
warehouses[0].move_equipment(warehouses[1], equipment[2], 2)
# HR
warehouses[0].move_equipment(warehouses[2], equipment[0], 2)
warehouses[0].move_equipment(warehouses[2], equipment[1], 1)
warehouses[0].move_equipment(warehouses[2], equipment[2], 1)
# IT
warehouses[0].move_equipment(warehouses[3], equipment[0], 4)
warehouses[0].move_equipment(warehouses[3], equipment[1], 2)
warehouses[0].move_equipment(warehouses[3], equipment[2], 1)
# Выводим состояние всех складов
for i in range(len(warehouses)):
    warehouses[i].list_equipment()

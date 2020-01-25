"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

"""

people = dict()
try:
    with open('task03_input.txt', 'r', encoding='utf8') as f:
        for line in f:
            person, salary = line.split()
            people.update({person: float(salary)})
    sum_salary = 0              # Суммарная зарплата
    low_salary_people = []      # Кол-во сотрудников с низким окладом
    for k, v in people.items():
        sum_salary += v
        if v < 20000:
            low_salary_people.append(k)
    print(f'Оклад ниже 20000 у {len(low_salary_people)} сотрудников :')
    [print(i) for i in low_salary_people]
    print(f'Средняя величина дохода сотрудников равна {sum(people.values())/len(people):.2f}')
except IOError:
    print('Произошла ошибка ввода-вывода!')
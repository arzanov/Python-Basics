"""
Программа создаёт колоду карт и сдаёт пользователю произвольное количество.
"""


from itertools import count, cycle
from random import shuffle


def deck_init():
    """
    Инициализирует колоду карт

    :return: Возвращает колоду в виде списка карт, упорядоченных по старшинству.
    """
    deck = []
    suits = ['Пики', 'Трефы', 'Бубны', 'Червы']  # Инициализируем масти
    highs = ['Валет', 'Дама', 'Король', 'Туз']   # Старшие карты
    card_suite = cycle(suits)
    for i in count(2):                          # Создаем младшие карты
        if i > 10:
            break
        else:
            for j in range(4):                  # Создаем старшие карты
                deck.append(str(i) + ' ' + next(card_suite))
    for i in range(len(highs)):
        for j in range(4):
            deck.append(highs[i] + ' ' + next(card_suite))
    return deck


def deal(deck, to_deal):
    """
    Функция генератор, сдающая по 1 карте to_deal раз.

    :param deck: список с колодой из которой сдаются карты
    :param to_deal: количество сдаваемых карт
    :return: возвращает карту
    """
    for i in range(to_deal):
        yield deck.pop()


my_deck = deck_init()   # Создаём колоду
shuffle(my_deck)        # Перемешиваем карты
my_hand = []            # Карты на руках
flag = False
while not flag:
    try:
        n = int(input('Сколько карт вам сдать? - '))
        if 0 <= n <= 52:
            flag = True
        else:
            print('Необходимо ввести целое число от 0 до 52. Попробуйте снова.')
    except ValueError:
        print('Необходимо ввести целое число от 0 до 52. Попробуйте снова.')
for i in deal(my_deck, n):
    my_hand.append(i)
print(f'Ваши карты: {my_hand}')
print(f'В колоде осталось {len(my_deck)} карт(ы)')
while True:
    if len(my_deck) == 0:
        print('В колоде закончились карты.')
        break
    else:
        more = input('Еще карту? (y/n): ')
        if more == 'y':
            my_hand.append(*list(deal(my_deck, 1)))
            print(f'Ваши карты: {my_hand}')
            print(f'В колоде осталось {len(my_deck)} карт(ы)')
        elif more == 'n':
            break
        else:
            print('Необходимо ввести y или n.')

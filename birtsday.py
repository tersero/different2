# Перед вами программа, которая показывает майских именинников в алфавитном порядке.

from collections import namedtuple

Date = namedtuple('Date', 'year,month,day')

count = int(input('Введите количество именинников '))

birth_dates = {}
print('Вводите данные в формате: имя год месяц день (через пробел)')
for _ in range(count):
    name, year, month, day = input().split(' ')
    birth_dates[name] = Date(int(year), int(month), int(day))

born_in_may = [
    name
    for name, date in birth_dates.items()
    if date.month == 5
]

born_in_may.sort()
print('Родились в мае:', *born_in_may)
#t(*born_in_may)
"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

from random import sample

def find_index(lst, span):
    result = []
    min, max = int(span[0]), int(span[1])
    for i, val in enumerate(lst):
        if val >= min and val <= max:
            result.append(i)
    if len(result) < 1:
        result = "нет"
    return result

lst = sample(range(0, 101), 20)
print(f"Список значений: {lst}")
span = input("Задайте min и max значения диапизона через пробел: ").split()
print(f"Индексы значений в заданном зиапазоне: {find_index(lst, span)}")

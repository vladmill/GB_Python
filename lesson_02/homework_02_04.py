"""
Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

n = input("Введите целые числа через пробел: ").split()
for i in range(0, len(n), 2):
    if i + 1 < len(n):
        n[i], n[i+1] = n[i+1], n[i]
n = " ".join(n)
print(f"{n}")

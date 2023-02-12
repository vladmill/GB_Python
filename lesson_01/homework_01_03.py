"""
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = input("Введите целое положительное число: ")
nn = n + n
nnn = n + n + n
result = int(n) + int(nn) + int(nnn)
print(f"n + nn + nnn = {result}")

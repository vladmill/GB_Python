"""
Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""

from math import pi
d = float(input("Задайте точность числа Пи: "))
if d < 1:
    n = int(len(str(d).split('.')[1]))
else:
    n = int(str(d).split('.')[0])

print(f"Результат: {round(pi, n)}")

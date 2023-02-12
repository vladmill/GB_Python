"""
Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N.
"""

n = int(input("Введите число: "))
lst = []
d = 2
while d * d <= n:
    if n % d == 0:
        lst.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    lst.append(n)

print(lst)

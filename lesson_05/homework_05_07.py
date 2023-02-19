"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def input_num():
    try:
        num = int(input(f"Введите натуральное число: "))
    except ValueError:
        print("Необходимо ввести натуральное число. Попробуйте еще раз.")
        input_num()
    else:
        return num


def sum_str(num):
    if num == 1:
        return "1"
    return f"{sum_str(num - 1)}+{num}"


def sum_num(num):
    if num == 1:
        return 1
    return num + sum_num(num - 1)


def check_equality():
    num = input_num()
    if sum_num(num) == num * (num + 1) / 2:
        print("True")
        print(f"{sum_str(num)} = {num}({num}+1)/2")
        print(f"{sum_num(num)} = {num * (num + 1) / 2}")
    else:
        print("False")
        print(f"{sum_str(num)} != {num}({num}+1)/2")
        print(f"{sum_num(num)} != {num * (num + 1) / 2}")

check_equality()

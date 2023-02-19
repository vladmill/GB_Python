"""
Задача 30: Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""


def input_num():
    try:
        param = {"first": int(input("Введите первый элемент: ")),
                 "differ": int(input("Введите разность: ")),
                 "length": int(input("Введите количество элементов: "))}
    except ValueError:
        print("Необходимо ввести натуральные числа. Попробуйте еще раз.")
        input_num()
    else:
        return param


def create_list(param):
    result = []
    for i in range(param["length"]):
        n = i + 1
        result.append(param["first"] + (n - 1) * param["differ"])
    print(result)


create_list(input_num())

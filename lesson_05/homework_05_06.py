"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""


def input_num(attempt):
    try:
        num = int(input(f"{attempt} попытка: "))
    except ValueError:
        print("Необходимо ввести целое число от 0 до 100. Попробуйте еще раз.")
        input_num(attempt)
    else:
        if num < 0 or num > 100:
            print("Необходимо ввести число от 0 до 100. Попробуйте еще раз.")
            input_num(attempt)
        else:
            return num


def guess_num(x, attempt, i=0):
    if i < attempt:
        i += 1
        num_try = input_num(i)
        if num_try < x:
            print(f"Загаданное чило больше {num_try}")
            guess_num(x, attempt, i)
        elif num_try > x:
            print(f"Загаданное чило меньше {num_try}")
            guess_num(x, attempt, i)
        else:
            print(f"Ура! Вы угадали, это {x}")
    else:
        print(f"Вы не справились. Было загадано число {x}")

import random

num_from = 0
num_to = 100
attempt = 10
num_rand = random.randint(num_from, num_to)
print(f"Угадайте число от {num_from} до {num_to} за {attempt} попыток")
guess_num(num_rand, attempt)

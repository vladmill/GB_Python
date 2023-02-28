"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


def print_type_elem(lst):
    """Вывод типа, длины и содержимого"""
    for elem in lst:
        print(f"Тип: {type(elem)}, Длина: {len(elem)}, "
              f" Содержимое: \u00AB{elem}\u00BB")


lst_ch = ["class", "function", "method"]
lst_by = [bytes(elem, encoding='utf-8') for elem in lst_ch]

"""Если все-таки обязательно использовать маркировку b'' """
lst_mb = [b"class", b"function", b"method"]


print("Буквенный формат:")
print_type_elem(lst_ch)
print("Байтовый формат:")
print_type_elem(lst_by)
print("Байтовый формат b'':")
print_type_elem(lst_mb)

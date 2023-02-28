"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b''
(без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


class IsCyrillic(Exception):
    """Класс-исключение"""

    def __init__(self, txt):
        self.txt = txt


def check_cyrillic(lst):
    """проверка на кирилицу"""
    lst_by = [bytes(elem, encoding='utf-8') for elem in lst_ch]
    length = len(lst)
    for i in range(length):
        try:
            if len(lst[i]) != len(lst_by[i]):
                raise IsCyrillic(f"\u00AB{lst[i]}\u00BB - невозможно записать "
                                 f"в байтовом типе с помощью маркировки b''")
        except IsCyrillic as err:
            print(err)


lst_ch = ["attribute", "класс", "функция", "type"]

check_cyrillic(lst_ch)

"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

import chardet


def decode_lst(lst):
    """Конвертация из байтов в строки"""
    result = []
    for elem in lst:
        cur_enc = chardet.detect(elem)['encoding']
        result.append(elem.decode(cur_enc))
    return result


lst_ch = ["разработка", "администрирование", "protocol", "standard"]
lst_en = [elem.encode("utf-8") for elem in lst_ch]
lst_de = decode_lst(lst_en)

print(f"str: {lst_ch}")
print(f"str > bytes: {lst_en}")
print(f"bytes > str: {lst_de}")

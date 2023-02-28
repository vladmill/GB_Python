"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

ARGS = [
    ['ping', 'yandex.ru'],
    ['ping', 'youtube.com']
]

for arg in ARGS:
    PING = subprocess.Popen(arg, stdout=subprocess.PIPE)
    for line in PING.stdout:
        cur_enc = chardet.detect(line)['encoding']
        print(line.decode(cur_enc))

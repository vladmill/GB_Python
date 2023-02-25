"""
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет)
и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    __color = ["красный", "Жёлтый", "Зелёный"]

    def __init__(self, t_red, t_yellow, t_green):
        self.timer = [t_red, t_yellow, t_green]

    def running(self):
        for i in range(len(self.__color)):
            print(self.__color[i])
            sleep(self.timer[i])
            print(f"прошло {self.timer[i]} сек.")


if __name__ == '__main__':
    obj_tl = TrafficLight(7, 2, 5)
    obj_tl.running()
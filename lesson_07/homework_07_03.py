"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также
через перегрузку str str(self) - вызывается функциями str, print и format.
Возвращает строковое представление объекта.
"""


class Worker:
    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float,
            bonus: float
    ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.surname + " " + self.name

    def get_total_income(self):
        return sum(self._income.values())

    def __str__(self):
        print("объект")


if __name__ == '__main__':
    data_1 = {
        'name': 'Иван',
        'surname': 'Иванов',
        'position': 'Разработчик',
        'wage': 100000,
        'bonus': 50000
    }
    data_2 = {
        'name': 'Пётр',
        'surname': 'Петров',
        'position': 'Аналитик',
        'wage': 120000,
        'bonus': 40000
    }

    unit_1 = Position(**data_1)
    unit_2 = Position(**data_2)

    print(f"Полное имя: {unit_1.get_full_name()}\n"
          f"Должность: {unit_1.position} \n"
          f"Доход: {unit_1.get_total_income()}\n")

    print(unit_2)


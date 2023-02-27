"""
Создать не менее двух дескрипторов для атрибутов классов,
которые вы создали ранее в ДЗ
"""


class NotNegative:
    """Класс для дескрипторов не меньше нуля"""

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class NotDel:
    """Класс для неудаляемых дескрипторов"""

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise ValueError("Невозможно удалить атрибут")

    def __set_name__(self, owner, name):
        self.name = name


class Worker:
    """Базовый класс"""
    wage = NotNegative()
    name = NotDel()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """Класс на базе Worker"""

    def get_full_name(self):
        return self.surname + " " + self.name

    def get_total_income(self):
        return sum(self._income.values())

    def __str__(self):
        return f"Полное имя: {self.get_full_name()}\n" \
               f"Должность: {self.position} \n" \
               f"Доход: {self.get_total_income()}\n"


if __name__ == "__main__":
    data_1 = {
        "name": "Иван",
        "surname": "Иванов",
        "position": "Разработчик",
        "wage": 100000,
        "bonus": 50000
    }

    unit_1 = Position(**data_1)

    """Проверка дескрипторов"""
    #unit_1.wage = -100000
    delattr(unit_1, "name")

    print(unit_1)

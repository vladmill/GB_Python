"""
Создать метакласс для паттерна Синглтон
"""


class Singleton(type):
    """Метакласс гарантирующий, что будет создан единственный экземпляр
    некоторого класса и предоставляющий глобальную точку доступа
    к этому экземпляру"""

    link = None

    def __call__(cls, *args, **kvargs):
        if cls.link is None:
            cls.link = type.__call__(cls, *args, **kvargs)
            return cls.link
        return cls.link


class MyClassA(metaclass=Singleton):
    """test"""


class MyClassB(metaclass=Singleton):
    """test"""


a = MyClassA()
b = MyClassB()
print(a is b, end="\n\n")

c = MyClassA()
d = MyClassB()
print(a is c)
print(b is d)

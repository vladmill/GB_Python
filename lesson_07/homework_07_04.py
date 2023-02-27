"""
Задание 4.
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода
матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения
двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом
первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, data):
        self.matrix = data

    def __str__(self):
        # m_str = ""
        # for i in range(len(self.matrix)):
        #     m_str += '\t'.join(map(str, self.matrix[i])) + '\n'
        # return m_str
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix]) \
               + '\n'

    def __add__(self, other):
        row = len(self.matrix)
        cols = len(self.matrix[0])
        result = [[0] * row for i in range(cols)]
        for i in range(row):
            for j in range(cols):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)


if __name__ == '__main__':
    data_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data_2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

    m_1 = Matrix(data_1)
    m_2 = Matrix(data_2)

    print(f"{m_1}\n{m_2}")
    print(m_1 + m_2)

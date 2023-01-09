import sys

from linear_independence import maximum_linear_independence


class Matrix:

    def __init__(self, count_rows: int, count_columns: int, matrix: list):
        self.count_rows = count_rows
        self.count_columns = count_columns
        self.matrix = matrix

    def __add__(self, other):
        if type(other) == type(self):
            if self.count_rows == other.count_rows and self.count_columns == other.count_columns:
                return Matrix(self.count_rows, self.count_columns,
                              [[self.matrix[row_index][column_index] + other.matrix[row_index][column_index]
                                for column_index in range(self.count_columns)] for row_index in range(self.count_rows)])
            else:
                raise ValueError
        else:
            raise TypeError

    def __sub__(self, other):
        if type(other) == type(self):
            return self.__add__(other * -1)
        else:
            raise TypeError

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Matrix(self.count_rows, self.count_columns,
                          [[self.matrix[row_index][column_index] * other for column_index in range(self.count_columns)] for row_index in range(self.count_rows)])
        elif type(other) == type(self):
            if self.count_columns == other.count_rows:
                return Matrix(self.count_rows, other.count_columns,
                              [[sum([self.matrix[row_index][i] * other.matrix[i][column_index] for i in range(self.count_columns)]) for column_index in range(other.count_columns)] for row_index in range(self.count_rows)])
            else:
                raise ValueError
        else:
            raise TypeError

    def transponiert(self):
        return Matrix(self.count_columns, self.count_rows,
                      [[self.matrix[row_index][column_index] for row_index in range(self.count_rows)] for column_index in range(self.count_columns)])

    def rank(self) -> int:
        return maximum_linear_independence(self.get_column_vectors())

    def get_column_vectors(self) -> list:
        return self.transponiert().matrix

    def switch_columns(self, column_a: int, column_b: int):
        matrix_array: list = self.get_column_vectors()
        old_column_a = matrix_array[column_a].copy()
        matrix_array[column_a] = matrix_array[column_b].copy()
        matrix_array[column_b] = old_column_a
        return Matrix(self.count_columns, self.count_rows, matrix_array).transponiert()

    def switch_rows(self, row_a: int, row_b: int):
        matrix_array: list = self.matrix.copy()
        matrix_array[row_a] = self.matrix[row_b].copy()
        matrix_array[row_b] = self.matrix[row_a].copy()
        return Matrix(self.count_rows, self.count_columns, matrix_array)

    def concatenate(self, other):
        if type(self) == type(other):
            if self.count_rows == other.count_rows:
                return Matrix(self.count_rows, self.count_columns + other.count_columns,
                              [self.matrix[row_index] + other.matrix[row_index] for row_index in range(self.count_rows)])
            raise ValueError
        raise TypeError

    def count_non_zero_rows(self) -> int:
        count = 0
        for row in self.matrix:
            for value in row:
                if value != 0:
                    count += 1
                    break
        return count

    def __str__(self):
        str_columns = []
        for row_index in range(self.count_rows):
            str_columns.append("|{}|".format(" ".join(map(str, self.matrix[row_index]))))

        return "\n" + "\n".join(str_columns)

    def multiply_row(self, to_multiplied_row_index: int, scalar):
        new_matrix = [[self.matrix[row_index][column_index] * (1 if row_index != to_multiplied_row_index else scalar)
                       for column_index in range(self.count_columns)] for row_index in range(self.count_rows)]
        return Matrix(self.count_rows, self.count_columns, new_matrix)

    def set_value(self, row: int, column: int, value: int):
        matrix_array = self.matrix.copy()
        matrix_array[row][column] = value
        return Matrix(self.count_rows, self.count_columns, matrix_array)


def identity_matrix(count_rows: int, count_columns: int) -> Matrix:
    return Matrix(count_rows, count_columns,
                  [[1 if row_index == column_index else 0 for column_index in range(count_columns)] for row_index in range(count_rows)])


if __name__ == "__main__":
    m1 = Matrix(2, 2, [[0, -1], [3, 4]])
    m2 = Matrix(2, 2, [[23, 1], [4, -2]])
    print(m2 + m1)
    print(m1 * 2.23)
    print(m1 * m2, "\n")

    t1 = Matrix(3, 2, [[2, 5], [1, 0], [3, 1]])
    t2 = Matrix(2, 5, [[8, 1, 2, 3, 0], [0, 2, 4, 0, 1]])
    print(t1 * t2 * 0)
    print(t1.transponiert())
    print(m1)
    print(m1.transponiert())

    print("Test")
    print((m1+m2).transponiert())
    print(m1.transponiert() + m2.transponiert())

    print("Test")
    print((t1 * 3).transponiert())
    print(t1.transponiert() * 3)

    print("Test")
    print((t1 * t2).transponiert())
    print(t2.transponiert() * t1.transponiert())

    print(t1.transponiert().transponiert())

    print(t1.get_column_vectors())

    print(t1.multiply_row(1, 2).multiply_row(0, -23.3))

    matrix = t1 * t2
    k = 0
    print(matrix * Matrix(5, 5, [[2, 0, 0, 0, 0], [0, 1, 0, 0,0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
    print(identity_matrix(3, 3))
    print(identity_matrix(5, 3))
    print(identity_matrix(3, 5))
    print(m1 - m2)

    print((t1 * t2).switch_rows(1, 0))
    print(m1.concatenate(m2))
    sys.exit()
    matrix = matrix * Matrix(matrix.count_columns, 1,
                             [[23] for i in range(matrix.count_columns)])
    mult_matrix = 2
    print(matrix)

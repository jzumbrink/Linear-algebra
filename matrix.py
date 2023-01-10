import sys


class Matrix:

    def __init__(self, count_rows: int, count_columns: int, matrix: list):
        self.count_rows = count_rows
        self.count_columns = count_columns
        self.matrix = matrix

    # The addition works only with another matrix of the same dimension
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

    # The subtraction uses the already implemented addition after multiplying the other element with -1
    def __sub__(self, other):
        if type(other) == type(self):
            return self.__add__(other * -1)
        else:
            raise TypeError

    # This function implements both the matrix multiplication and the scalar multiplication.
    # Please note that the scalar has to be the second element in the multiplication.
    # (mathematically there is no difference)
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

    def transpose(self):
        return Matrix(self.count_columns, self.count_rows,
                      [[self.matrix[row_index][column_index] for row_index in range(self.count_rows)] for column_index in range(self.count_columns)])

    # set the value of a single cell
    def set_value(self, row: int, column: int, value: int):
        matrix_array = self.matrix.copy()
        matrix_array[row][column] = value
        return Matrix(self.count_rows, self.count_columns, matrix_array)

    def get_column_vectors(self) -> list:
        return self.transpose().matrix

    def switch_columns(self, column_a: int, column_b: int):
        matrix_array: list = self.get_column_vectors()
        old_column_a = matrix_array[column_a].copy()
        matrix_array[column_a] = matrix_array[column_b].copy()
        matrix_array[column_b] = old_column_a
        return Matrix(self.count_columns, self.count_rows, matrix_array).transpose()

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

    def multiply_row(self, to_multiplied_row_index: int, scalar):
        new_matrix = [[self.matrix[row_index][column_index] * (1 if row_index != to_multiplied_row_index else scalar)
                       for column_index in range(self.count_columns)] for row_index in range(self.count_rows)]
        return Matrix(self.count_rows, self.count_columns, new_matrix)

    def is_zero_row(self, row: int) -> bool:
        for value in self.matrix[row]:
            if value != 0:
                return False
        return True

    def is_zero_column(self, column: int, start_row: int=0) -> bool:
        for row in self.matrix[start_row:]:
            if row[column] != 0:
                return False
        return True

    def __str__(self):
        str_columns = []
        for row_index in range(self.count_rows):
            str_columns.append("|{}|".format(" ".join(map(str, self.matrix[row_index]))))

        return "\n" + "\n".join(str_columns)


def identity_matrix(count_rows: int, count_columns: int) -> Matrix:
    return Matrix(count_rows, count_columns,
                  [[1 if row_index == column_index else 0 for column_index in range(count_columns)] for row_index in range(count_rows)])


def zero_matrix(count_rows: int, count_columns: int) -> Matrix:
    return Matrix(count_rows, count_columns, [[0 for _ in range(count_columns)] for __ in range(count_rows)])


if __name__ == "__main__":
    m1 = Matrix(2, 2, [[0, -1], [3, 4]])
    m2 = Matrix(2, 2, [[23, 1], [4, -2]])
    print(m2 + m1)
    print(m1 * 2.23)
    print(m1 * m2, "\n")

    t1 = Matrix(3, 2, [[2, 5], [1, 0], [3, 1]])
    t2 = Matrix(2, 5, [[8, 1, 2, 3, 0], [0, 2, 4, 0, 1]])
    print(t1 * t2 * 0)
    print(t1.transpose())
    print(m1)
    print(m1.transpose())

    print("Test")
    print((m1+m2).transpose())
    print(m1.transpose() + m2.transpose())

    print("Test")
    print((t1 * 3).transpose())
    print(t1.transpose() * 3)

    print("Test")
    print((t1 * t2).transpose())
    print(t2.transpose() * t1.transpose())

    print(t1.transpose().transpose())

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
    print(zero_matrix(2, 6).is_zero_row(1))
    print(m1.is_zero_row(0))

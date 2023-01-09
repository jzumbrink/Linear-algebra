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

    def __str__(self):
        str_columns = []
        for row_index in range(self.count_rows):
            str_columns.append("|{}|".format(" ".join(map(str, self.matrix[row_index]))))

        return "\n" + "\n".join(str_columns)


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



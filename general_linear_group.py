from matrix import *
from linear_independence import *


"""
A square matrix A is called invertible if another matrix B exists, such that A*B=identity matrix.
This property is equivalent to rank(A)=count of rows/columns
"""
def is_invertible(m: Matrix) -> bool:
    if m.count_rows == m.count_columns:
        return rank(m) == m.count_rows
    else:
        raise ValueError


if __name__ == "__main__":
    m1 = Matrix(3, 3, [[1, 3, 2], [2, 0, 1], [3, 1, 1]])
    m2 = Matrix(2, 2, [[1, 1], [0,0]])
    print("Is m1 invertible: {}".format(is_invertible(m1)))
    print("Is m2 invertible: {}".format(is_invertible(m2)))

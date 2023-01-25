from matrix import *
from gauss import *


def determinant(m: Matrix) -> float:
    return gaussian_elim(m, {"block": ["E2"]}).diagonal_product()


if __name__ == "__main__":
    m1 = Matrix(2, 2, [[2, 1], [1, 2]])
    print(determinant(m1))

    m2 = Matrix(3, 3, [[1, 2, 3], [1, 1, 2], [1, 1, 1]])
    print(determinant(m2))
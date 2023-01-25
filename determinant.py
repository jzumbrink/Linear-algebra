from matrix import *
from gauss import *


def determinant(m: Matrix) -> float:
    options = {"block": ["E2", "E4"], "count_row_changes": 0}
    return gaussian_elim(m, options).diagonal_product() * (-1)**options["count_row_changes"]


if __name__ == "__main__":
    m1 = Matrix(2, 2, [[2, 1], [1, 2]])
    print(determinant(m1))

    m2 = Matrix(3, 3, [[1, 2, 3], [1, 1, 2], [1, 1, 1]])
    print(determinant(m2))

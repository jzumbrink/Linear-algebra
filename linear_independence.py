from matrix import *
from gauss import *


def rank(input_matrix: Matrix) -> int:
    return solve_system_of_linear_equations(input_matrix, zero_matrix(input_matrix.count_rows, 1))[0].count_non_zero_rows()


if __name__ == "__main__":
    a = Matrix(2, 2, [[1, 0], [1, 1]])
    t1 = Matrix(3, 2, [[2, 5], [1, 0], [3, 1]])
    t2 = Matrix(2, 5, [[8, 1, 2, 3, 0], [0, 2, 4, 0, 1]])
    e1 = Matrix(3, 4, [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]])
    print(a)
    print("rank(A) = {}".format(rank(a)))
    print(t1)
    print("rank(T1) = {}".format(rank(t1)))
    print(t2)
    print("rank(T2) = {}".format(rank(t2)))
    print(e1)
    print("rank(E1) = {}".format(rank(e1)))

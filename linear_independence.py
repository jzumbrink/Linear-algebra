from matrix import *
from gauss import *

"""
The rank of a matrix A is the maximum count of linear independent columns of A.
This is the same as the number of non-zero rows in reduced row echelon form.

So to determine the rank of a matrix, the gaussian algorithm is used to bring the matrix in the reduced row echelon form.
After that, it is simple to count the number of non zero rows.
"""


def rank(input_matrix: Matrix) -> int:
    return gaussian_elimination(input_matrix, zero_matrix(input_matrix.count_rows, 1))[0].count_non_zero_rows()


if __name__ == "__main__":
    a = Matrix(2, 2, [[1, 0], [1, 1]])
    t1 = Matrix(3, 2, [[2, 5], [1, 0], [3, 1]])
    t2 = Matrix(2, 5, [[8, 1, 2, 3, 0], [0, 2, 4, 0, 1]])
    e1 = Matrix(3, 4, [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]])
    e2 = Matrix(4, 3, [[1, -1, 0], [1, 3, 2], [2, 0, 1], [3, 1, 1]])
    print(a)
    print("rank(A) = {}".format(rank(a))) # rank 2
    print(t1)
    print("rank(T1) = {}".format(rank(t1))) # rank 2
    print(t2)
    print("rank(T2) = {}".format(rank(t2)))  # rank 2
    print(e1)
    print("rank(E1) = {}".format(rank(e1)))  # rank 2
    print(e2)
    print("rank(EE) = {}".format(rank(e2)))  # rank 3

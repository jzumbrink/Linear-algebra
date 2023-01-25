from matrix import Matrix


"""
Gaussian elimination
Using four types of elementary row operations
- E1: swap positions of two rows
- E2: multiply a row by a non-zero scalar
- E3: substitute a row with the sum of this row and the multiple of another row
- E4: swap positions of two columns
"""
def gaussian_elimination(matrix: Matrix, right_side: Matrix, options: dict = {}):
    if matrix.count_rows == right_side.count_rows:
        for k in range(min(matrix.count_rows, matrix.count_columns)):
            # E4
            if matrix.is_zero_column(k, k):
                for l in range(k + 1, matrix.count_rows):
                    if not matrix.is_zero_column(l, k + 1):
                        # switch column k with column l
                        matrix = matrix.switch_columns(k, l)
                        break
                else:
                    # algorithm has terminated
                    break

            # E1
            if matrix.matrix[k][k] == 0:
                for l in range(k + 1, matrix.count_rows):
                    if matrix.matrix[l][k] != 0:
                        # swap row k with row l
                        matrix = matrix.switch_rows(k, l)
                        right_side = right_side.switch_rows(k, l)
                        break
                else:
                    # should never be triggered
                    raise RuntimeError

            # E2
            if matrix.matrix[k][k] != 1 and ("block" not in options or "E2" not in options["block"]):
                current_diagonal_value = 1 / matrix.matrix[k][k]
                matrix = matrix.multiply_row(k, current_diagonal_value)
                right_side = right_side.multiply_row(k, current_diagonal_value)

            # E3
            for i in range(k + 1, matrix.count_rows):
                if matrix.matrix[i][k] != 0:
                    matrix -= Matrix(matrix.count_rows, matrix.count_columns,
                                     [[0 for _ in range(matrix.count_columns)] if row_index != i else matrix.matrix[k]
                                      for row_index in range(matrix.count_rows)]) * matrix.matrix[i][k] * (1/matrix.matrix[k][k])
                    right_side = right_side.set_value(i, 0, right_side.matrix[i][0] - right_side.matrix[k][0])

        return matrix, right_side
    else:
        ValueError


def gaussian_elim(matrix: Matrix, options: dict = {}) -> Matrix:
    return gaussian_elimination(matrix, Matrix(matrix.count_rows, 1, [[0] for _ in range(matrix.count_rows)]), options)[0]


if __name__ == "__main__":
    m1 = Matrix(3, 3, [[1, 1, 1], [0, 0, 1], [0, 1, 0]])
    m2 = Matrix(3, 3, [[2, 3, 0], [1, 0, 0], [0, 0, 0]])
    m3 = Matrix(3, 3, [[2, 3, 0], [0, 0, 0], [1, 0, 0]])
    r0 = Matrix(3, 1, [[3], [2], [1]])
    print("\n".join(map(str, gaussian_elimination(m3, r0))))

    z = Matrix(6, 8, [
        [1, 0, 3, 8, 1, 0, 3, 8],
        [0, 2, 1, 1, 0, 2, 1, 1],
        [0, 2, 1, 2, 0, 2, 1, 2],
        [1, -4, 1, 5, 1, -4, 1, 5],
        [1, 0, -1, 0, 0, 0, 0, 0],
        [2, -2, 5, 13, 0, 0, 0, 0],
    ])
    rz = Matrix(6, 1, [[0] for _ in range(6)])
    print("\n".join(map(str, gaussian_elimination(z, rz))))

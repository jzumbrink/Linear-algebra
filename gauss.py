from matrix import Matrix


def solve_system_of_linear_equations(matrix: Matrix, right_side: Matrix):
    if matrix.count_rows == right_side.count_rows:
        for k in range(min(matrix.count_rows, matrix.count_columns)):
            if sum([matrix.matrix[i][k] for i in range(k, matrix.count_rows)]) == 0:
                for l in range(k+1, matrix.count_columns):
                    if sum([matrix.matrix[i][l] for i in range(k, matrix.count_rows)]) != 0:
                        # switch column k with column l
                        matrix = matrix.switch_columns(k, l)
                        break
                else:
                    # algorithm has terminated
                    break

            if matrix.matrix[k][k] == 0:
                # tausche Zeile mit anderen Zeile, wenn möglich
                for row_index in range(k + 1, matrix.count_rows):
                    if matrix.matrix[row_index][k] != 0:
                        matrix = matrix.switch_rows(k, row_index)
                        right_side = right_side.switch_rows(k, row_index)
                        break
                else:
                    # should never be triggered
                    raise RuntimeError

            if matrix.matrix[k][k] != 1:
                matrix = matrix.multiply_row(k, 1/matrix.matrix[k][k])
                right_side = right_side.multiply_row(k, 1/matrix.matrix[k][k])

            #k_4
            for i in range(k+1, matrix.count_rows):
                if matrix.matrix[i][k] != 0:
                    matrix -= Matrix(matrix.count_rows, matrix.count_columns,
                                     [[0 for _ in range(matrix.count_columns)] if row_index != i else matrix.matrix[k] for row_index in range(matrix.count_rows)]) * matrix.matrix[i][k]
                    right_side = right_side.set_value(i, 0, right_side.matrix[i][0] - right_side.matrix[k][0])

        return matrix, right_side
    else:
        ValueError


if __name__ == "__main__":
    m1 = Matrix(3, 3, [[1, 1, 1], [0, 0, 1], [0, 1, 0]])
    m2 = Matrix(3, 3, [[2, 3, 0], [1, 0, 0], [0, 0, 0]])
    m3 = Matrix(3, 3, [[2, 3, 0], [0, 0, 0], [1, 0, 0]])
    r0 = Matrix(3, 1, [[3], [2], [1]])
    solve_system_of_linear_equations(m3, r0)

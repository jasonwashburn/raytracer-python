from __future__ import annotations

from math import isclose


class Matrix:
    def __init__(self, elements: list[list[float | int]]):
        self.elements = elements
        self.rows = len(elements)
        self.columns = len(elements[0])

    def __getitem__(self, idx: tuple[int, int]) -> float | int:
        return self.elements[idx[0]][idx[1]]

    def __setitem__(self, idx: tuple[int, int], value: int | float) -> None:
        self.elements[idx[0]][idx[1]] = value

    def __repr__(self) -> str:
        return f"Matrix({self.elements})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return False
        if len(self.elements) != len(other.elements):
            return False
        for row_index, row in enumerate(self.elements):
            if len(row) != len(other.elements[row_index]):
                return False
            for item_index, item in enumerate(row):
                if not isclose(item, other[row_index, item_index]):
                    return False

        return True

    @classmethod
    def new(cls, rows: int, cols: int, fill: int | float = 0) -> Matrix:
        elements = []
        for _row in range(rows):
            elements.append([fill for col in range(cols)])
        return Matrix(elements)

    def __mul__(self, other: Matrix | tuple) -> Matrix | tuple[float | int, ...]:
        if isinstance(other, Matrix):
            matrix = Matrix.new(self.rows, self.columns, 0)
            num_cols = other.columns

            for row_idx in range(self.rows):
                for col_idx in range(num_cols):
                    dot_product = 0.0
                    for k in range(num_cols):
                        dot_product += self[row_idx, k] * other[k, col_idx]
                    matrix[row_idx, col_idx] = dot_product
            return matrix
        else:
            result = [0.0 for _ in range(self.rows)]
            num_cols = 1

            for row_idx in range(len(other)):
                dot_product = 0.0
                for col_idx in range(self.columns):
                    dot_product += self[row_idx, col_idx] * other[col_idx]
                result[row_idx] = dot_product
            return tuple(result)


identity_matrix = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


def transpose(matrix: Matrix) -> Matrix:
    new_matrix = Matrix.new(rows=matrix.rows, cols=matrix.columns, fill=0.0)
    for row in range(matrix.rows):
        for col in range(matrix.columns):
            new_matrix[row, col] = matrix[col, row]

    return new_matrix

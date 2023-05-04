from math import isclose


class Matrix:
    def __init__(self, elements: list[list[float | int]]):
        self.elements = elements

    def __getitem__(self, idx: tuple[int, int]) -> float | int:
        return self.elements[idx[0]][idx[1]]

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

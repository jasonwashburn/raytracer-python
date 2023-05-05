import pytest

from raytracer.matrices import Matrix, identity_matrix


def test_constructing_and_inspecting_a_4x4_matrix() -> None:
    elements: list[list[int | float]] = [[1, 2, 3, 4], [5.5, 6.5, 7.5, 8.5], [9, 10, 11, 12], [13.5, 14.5, 15.5, 16.5]]
    matrix = Matrix(elements)
    assert matrix[0, 0] == 1
    assert matrix[0, 3] == 4
    assert matrix[1, 0] == 5.5
    assert matrix[1, 2] == 7.5
    assert matrix[2, 2] == 11
    assert matrix[3, 0] == 13.5
    assert matrix[3, 2] == 15.5


def test_2x2_matrix_ought_to_be_representable() -> None:
    elements: list[list[int | float]] = [[-3, 5], [1, -2.0]]
    matrix = Matrix(elements)
    assert matrix[0, 0] == -3
    assert matrix[0, 1] == 5
    assert matrix[1, 0] == 1
    assert matrix[1, 1] == -2


def test_3x3_matrix_out_to_be_representable() -> None:
    elements: list[list[int | float]] = [[-3, 5, 0], [1, -2, -7], [0, 1, 1.0]]
    matrix = Matrix(elements)
    assert matrix[0, 0] == -3
    assert matrix[1, 1] == -2
    assert matrix[2, 2] == 1


def test_construct_empty_matrix() -> None:
    matrix = Matrix.new(rows=3, cols=3, fill=0)
    assert matrix == Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])


def test_new_matrix_with_fill() -> None:
    matrix = Matrix.new(rows=3, cols=3, fill=1)
    assert matrix == Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])


def test_matrix_set_item() -> None:
    matrix = Matrix.new(rows=3, cols=3)
    matrix[1, 1] = 1
    assert matrix == Matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])


def test_matrix_rows() -> None:
    assert Matrix([[1, 2], [3, 4], [5, 6]]).rows == 3


def test_matrix_columns() -> None:
    assert Matrix([[1, 2], [3, 4], [5, 6]]).columns == 2


def test_matrix_equality_with_identical_matrices() -> None:
    elements: list[list[int | float]] = [
        [
            1.0,
            2,
            3,
            4,
        ],
        [
            5,
            6,
            7,
            8,
        ],
        [9, 8, 7, 6],
        [5, 4, 3, 2],
    ]
    matrix_a = Matrix(elements)
    matrix_b = Matrix(elements)
    assert matrix_a == matrix_b


def test_matrix_equality_with_nearly_identical_matrices() -> None:
    elements_a: list[list[int | float]] = [
        [
            1.0,
            2,
            3,
            4,
        ],
        [
            5,
            6,
            7,
            8,
        ],
        [9, 8, 7, 6],
        [5, 4, 3, 2],
    ]

    elements_b: list[list[int | float]] = [
        [
            1.000000000001,
            2,
            3,
            4,
        ],
        [
            5,
            6,
            7,
            8,
        ],
        [9, 8, 7, 6],
        [5, 4, 3, 2],
    ]
    matrix_a = Matrix(elements_a)
    matrix_b = Matrix(elements_b)
    assert matrix_a == matrix_b


@pytest.mark.parametrize(
    "elements_a, elements_b",
    [
        ([[1.0, 2], [3.0, 4]], [[2, 3.0], [4, 5.0]]),
        ([[1.0, 2], [3.0, 4]], [[1.0, 2], [3.0, 4], [1, 2]]),
        ([[1.0, 2], [3.0, 4]], [[1.0, 2], [3.0, 4, 1]]),
    ],
)
def test_matrix_equality_with_different_matrices(
    elements_a: list[list[int | float]], elements_b: list[list[int | float]]
) -> None:
    assert Matrix(elements_a) != Matrix(elements_b)


def test_matrix_equality_with_non_matrix() -> None:
    assert Matrix([[1, 2], [3, 4]]) != [[1, 2], [3, 4]]


def test_matrix_repr_builds_from_eval() -> None:
    assert eval(repr(Matrix([[1, 2], [3, 4]]))) == Matrix([[1, 2], [3, 4]])


def test_multiplying_two_matrices() -> None:
    matrix_a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
    matrix_b = Matrix(
        [
            [
                -2,
                1,
                2,
                3,
            ],
            [
                3,
                2,
                1,
                -1,
            ],
            [
                4,
                3,
                6,
                5,
            ],
            [
                1,
                2,
                7,
                8,
            ],
        ]
    )
    expected = Matrix(
        [
            [20, 22, 50, 48],
            [44, 54, 114, 108],
            [40, 58, 110, 102],
            [16, 26, 46, 42],
        ]
    )

    assert matrix_a * matrix_b == expected


def test_matrix_multiplied_by_a_tuple() -> None:
    matrix = Matrix(
        [
            [1, 2, 3, 4],
            [2, 4, 4, 2],
            [8, 6, 4, 1],
            [0, 0, 0, 1],
        ]
    )
    assert matrix * (1, 2, 3, 1) == (18, 24, 33, 1)


def test_multiplying_a_matrix_by_the_identity_matrix() -> None:
    matrix = Matrix(
        [
            [
                0,
                1,
                2,
                4,
            ],
            [
                1,
                2,
                4,
                8,
            ],
            [
                2,
                4,
                8,
                16,
            ],
            [4, 8, 16, 32],
        ]
    )
    assert matrix * identity_matrix == matrix


def multiplying_identity_matrix_by_a_tuple() -> None:
    a = (1, 2, 3, 4)
    assert identity_matrix * a == a

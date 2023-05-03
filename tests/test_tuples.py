from math import sqrt

import pytest

from raytracer.tuples import Color, Point, TupleFeature, Vector, clamp, cross, dot, magnitude, normalize, point, vector


def test_point() -> None:
    victim = Point((4.3, -4.2, 3.1, 1.0))
    assert victim.x == 4.3
    assert victim.y == -4.2
    assert victim.z == 3.1
    assert victim.w == 1.0
    assert victim.is_point
    assert not victim.is_vector


def test_vector() -> None:
    victim = Vector((4.3, -4.2, 3.1, 0))
    assert victim.x == 4.3
    assert victim.y == -4.2
    assert victim.z == 3.1
    assert victim.w == 0
    assert victim.is_vector
    assert not victim.is_point


def test_point_creates_tuples_with_w_equals_1() -> None:
    victim = point(4, -4, 3)
    assert victim == (4, -4, 3, 1)


def test_vector_creates_tuples_with_w_equals_0() -> None:
    victim = vector(4, -4, 3)
    assert victim == (4, -4, 3, 0)


def test_two_tuple_features_are_equal() -> None:
    assert TupleFeature((3, 2, 1, 0)) == TupleFeature((3, 2, 1, 0))


def test_adding_two_tuple_features() -> None:
    first = TupleFeature((3, -2, 5, 1))
    second = TupleFeature((-2, 3, 1, 0))
    assert first + second == TupleFeature((1, 1, 6, 1))


def test_subtracting_two_points() -> None:
    first = point(3, 2, 1)
    second = point(5, 6, 7)
    assert first - second == vector(-2, -4, -6)


def test_subtract_vector_from_point() -> None:
    assert point(3, 2, 1) - vector(5, 6, 7) == point(-2, -4, -6)


def test_subtracting_two_vectors() -> None:
    assert vector(3, 2, 1) - vector(5, 6, 7) == vector(-2, -4, -6)


def test_subtract_vector_from_zero() -> None:
    assert vector(0, 0, 0) - vector(1, -2, 3) == vector(-1, 2, -3)


def test_negating_a_tuple() -> None:
    assert -TupleFeature((1, -2, 3, -4)) == TupleFeature((-1, 2, -3, 4))


@pytest.mark.parametrize(
    "vector, expected",
    [
        (vector(4, 0, 0), vector(1, 0, 0)),
        (vector(1, 2, 3), vector(1 / sqrt(14), 2 / sqrt(14), 3 / sqrt(14))),
    ],
)
def test_normalize_vector(vector: Vector, expected: Vector) -> None:
    assert normalize(vector) == expected


def test_multiplying_tuple_by_a_scalar() -> None:
    assert TupleFeature((1, -2, 3, -4)) * 3.5 == TupleFeature((3.5, -7, 10.5, -14))


def test_multiplying_tuple_by_a_fraction() -> None:
    assert TupleFeature((1, -2, 3, -4)) * 0.5 == TupleFeature((0.5, -1, 1.5, -2))


def test_dividing_a_tuple_by_a_scalar() -> None:
    assert TupleFeature((1, -2, 3, -4)) / 2 == TupleFeature((0.5, -1, 1.5, -2))


@pytest.mark.parametrize(
    "vector, expected",
    [
        (vector(0, 1, 0), 1),
        (vector(0, 1, 0), 1),
        (vector(0, 0, 1), 1),
        (vector(1, 2, 3), sqrt(14)),
        (vector(-1, -2, -3), sqrt(14)),
    ],
)
def test_magnitude(vector: Vector, expected: int | float) -> None:
    assert magnitude(vector) == expected


def test_vector_repr_can_build_from_eval() -> None:
    victim = vector(1, 2, 3)
    assert eval(repr(victim)) == victim


def test_point_repr_can_build_from_eval() -> None:
    victim = point(1, 2, 3)
    assert eval(repr(victim)) == victim


def test_magnitude_of_normalized_vector_is_1() -> None:
    assert magnitude(normalize(vector(1, 2, 3))) == 1


def test_dot_product_of_two_tuples() -> None:
    assert dot(vector(1, 2, 3), vector(2, 3, 4)) == 20


def test_cross_product_of_two_vectors() -> None:
    vector_a = vector(1, 2, 3)
    vector_b = vector(2, 3, 4)
    assert cross(vector_a, vector_b) == vector(-1, 2, -1)
    assert cross(vector_b, vector_a) == vector(1, -2, 1)


def test_colors_are_red_green_blue_tuples() -> None:
    victim = Color(-0.5, 0.4, 1.7)
    assert victim.red == -0.5
    assert victim.green == 0.4
    assert victim.blue == 1.7


def test_color_repr_can_build_from_eval() -> None:
    assert eval(repr(Color(1, 2, 3))) == Color(1, 2, 3)


def test_color_equality() -> None:
    assert Color(1, 2, 3) == Color(1, 2, 3)


def test_adding_colors() -> None:
    assert Color(0.9, 0.6, 0.75) + Color(0.7, 0.1, 0.25) == Color(1.6, 0.7, 1.0)


def test_subtracting_colors() -> None:
    assert Color(0.9, 0.6, 0.75) - Color(0.7, 0.1, 0.25) == Color(0.2, 0.5, 0.5)


def test_multiplying_a_color_by_a_scalar() -> None:
    assert Color(0.2, 0.3, 0.4) * 2 == Color(0.4, 0.6, 0.8)


def test_multiplying_two_colors() -> None:
    assert Color(1, 0.2, 0.4) * Color(0.9, 1, 0.1) == Color(0.9, 0.2, 0.04)


def test_color_scaled_between() -> None:
    color = Color(0, 0.5, 1.5)
    assert color.scaled_between(0, 255) == (0, 128, 255)


def test_color_eq_returns_false_when_other_not_color() -> None:
    assert Color(0, 0, 0) != [0, 0, 0]


@pytest.mark.parametrize("number, clamp_min, clamp_max, expected", [(5, 0, 10, 5), (5, 10, 20, 10), (5, 0, 3, 3)])
def test_clamp(number: int, clamp_min: int, clamp_max: int, expected: int) -> None:
    assert clamp(number, clamp_min, clamp_max) == expected

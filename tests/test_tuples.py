from math import sqrt

import pytest

from raytracer.tuples import Point, TupleFeature, Vector, magnitude, normalize, point, vector


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

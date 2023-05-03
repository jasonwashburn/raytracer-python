from __future__ import annotations

from math import sqrt


class TupleFeature:
    def __init__(self, coords: tuple[float, float, float, float]) -> None:
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        self.w = coords[3]

    @property
    def is_point(self) -> bool:
        return self.w == 1

    @property
    def is_vector(self) -> bool:
        return self.w == 0

    def __eq__(self, other: object) -> bool:
        return self.coords == other

    def __add__(self, other: TupleFeature) -> TupleFeature:
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        w = self.w + other.w
        return TupleFeature((x, y, z, w))

    def __sub__(self, other: TupleFeature) -> TupleFeature:
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        w = self.w - other.w
        return TupleFeature((x, y, z, w))

    def __neg__(self) -> TupleFeature:
        x = -self.x
        y = -self.y
        z = -self.z
        w = -self.w
        return TupleFeature((x, y, z, w))

    def __mul__(self, other: float | int) -> TupleFeature:
        x = self.x * other
        y = self.y * other
        z = self.z * other
        w = self.w * other
        return TupleFeature((x, y, z, w))

    def __truediv__(self, other: float | int) -> TupleFeature:
        x = self.x / other
        y = self.y / other
        z = self.z / other
        w = self.w / other
        return TupleFeature((x, y, z, w))


class Point(TupleFeature):
    def __init__(self, coords: tuple[float, float, float, float]) -> None:
        super().__init__(coords)

    def __repr__(self) -> str:
        return f"Point({self.coords})"


class Vector(TupleFeature):
    def __init__(self, coords: tuple[float, float, float, float]) -> None:
        super().__init__(coords)

    def __repr__(self) -> str:
        return f"Vector({self.coords})"


def point(x: float, y: float, z: float, w: float = 1) -> Point:
    return Point((x, y, z, w))


def vector(x: float, y: float, z: float, w: float = 0) -> Vector:
    return Vector((x, y, z, w))


def magnitude(vec: Vector) -> int | float:
    return sqrt((vec.x**2) + (vec.y**2) + (vec.z**2) + (vec.w**2))


def normalize(vec: Vector) -> Vector:
    vector_magnitude = magnitude(vec)
    return vector(
        vec.x / vector_magnitude, vec.y / vector_magnitude, vec.z / vector_magnitude, vec.w / vector_magnitude
    )


def dot(vec_a: Vector, vec_b: Vector) -> int | float:
    return (vec_a.x * vec_b.x) + (vec_a.y * vec_b.y) + (vec_a.z * vec_b.z) + (vec_a.w * vec_b.w)

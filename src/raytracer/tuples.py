from __future__ import annotations


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


class Vector(TupleFeature):
    def __init__(self, coords: tuple[float, float, float, float]) -> None:
        super().__init__(coords)


def point(x: float, y: float, z: float) -> Point:
    return Point((x, y, z, 1))


def vector(x: float, y: float, z: float) -> Vector:
    return Vector((x, y, z, 0))

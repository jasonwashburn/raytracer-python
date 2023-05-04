from __future__ import annotations

from math import isclose, sqrt


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

    def __str__(self) -> str:
        x, y, z, w = self.coords
        return f"TupleFeature(x: {x}, y: {y}, z: {z}, w: {w})"


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


class Color:
    def __init__(self, red: float, green: float, blue: float) -> None:
        self.rgb = (red, green, blue)
        self.red = red
        self.green = green
        self.blue = blue

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Color):
            return False
        return isclose(self.red, other.red) and isclose(self.green, other.green) and isclose(self.blue, other.blue)

    def __repr__(self) -> str:
        return f"Color({self.red}, {self.green}, {self.blue})"

    def __add__(self, other: Color) -> Color:
        red = self.red + other.red
        green = self.green + other.green
        blue = self.blue + other.blue
        return Color(red, green, blue)

    def __sub__(self, other: Color) -> Color:
        red = self.red - other.red
        green = self.green - other.green
        blue = self.blue - other.blue
        return Color(red, green, blue)

    def scaled_between(self, scale_min: int, scale_max: int) -> tuple[int, int, int]:
        red = clamp(n=round(self.red * scale_max), clamp_min=scale_min, clamp_max=scale_max)
        green = clamp(n=round(self.green * scale_max), clamp_min=scale_min, clamp_max=scale_max)
        blue = clamp(n=round(self.blue * scale_max), clamp_min=scale_min, clamp_max=scale_max)
        return (red, green, blue)

    def __mul__(self, other: int | float | Color) -> Color:
        if isinstance(other, int | float):
            red = self.red * other
            green = self.green * other
            blue = self.blue * other
            return Color(red, green, blue)
        if isinstance(other, Color):
            red = self.red * other.red
            green = self.green * other.green
            blue = self.blue * other.blue
            return Color(red, green, blue)


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


def cross(vec_a: Vector, vec_b: Vector) -> Vector:
    return vector(
        vec_a.y * vec_b.z - vec_a.z * vec_b.y,
        vec_a.z * vec_b.x - vec_a.x * vec_b.z,
        vec_a.x * vec_b.y - vec_a.y * vec_b.x,
    )


def clamp(n: int, clamp_min: int, clamp_max: int) -> int:
    if n > clamp_max:
        return clamp_max
    if n < clamp_min:
        return clamp_min
    return n

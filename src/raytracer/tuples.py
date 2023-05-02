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

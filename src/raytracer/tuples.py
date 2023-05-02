class TupleFeature:
    def __init__(self, coords: tuple[float, float, float, float]) -> None:
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


class Point(TupleFeature):
    def __init__(self, coords: tuple[float, float, float, float]) -> None:
        super().__init__(coords)


class Vector(TupleFeature):
    def __init__(self, coords: tuple[float, float, float, float]) -> None:
        super().__init__(coords)

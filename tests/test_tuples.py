from raytracer.tuples import Point, Vector


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

from raytracer.canvas import Canvas, pixel_at, write_pixel
from raytracer.tuples import Color


def test_creating_a_canvas() -> None:
    victim = Canvas(10, 20)
    assert victim.width == 10
    assert victim.height == 20
    assert all(pixel == Color(0, 0, 0) for row in victim.pixels for pixel in row)


def test_writing_pixels_to_canvas() -> None:
    canvas = Canvas(10, 20)
    red = Color(1, 0, 0)
    write_pixel(canvas, 2, 3, red)
    assert pixel_at(canvas, 2, 3) == red

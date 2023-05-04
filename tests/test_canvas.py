from raytracer.canvas import Canvas, canvas_to_ppm, pixel_at, write_pixel
from raytracer.tuples import Color


def test_creating_a_canvas() -> None:
    victim = Canvas(10, 20)
    assert victim.width == 10
    assert victim.height == 20
    assert all(pixel == Color(0, 0, 0) for row in victim.pixels for pixel in row)


def test_creating_a_canvas_with_bg_color() -> None:
    victim = Canvas(width=10, height=20, bg_color=Color(1, 1, 1))
    assert victim.width == 10
    assert victim.height == 20
    assert all(pixel == Color(1, 1, 1) for row in victim.pixels for pixel in row)


def test_writing_pixels_to_canvas() -> None:
    canvas = Canvas(10, 20)
    red = Color(1, 0, 0)
    write_pixel(canvas, 2, 3, red)
    assert pixel_at(canvas, 2, 3) == red


def test_construction_ppm_header() -> None:
    canvas = Canvas(5, 3)
    ppm = canvas_to_ppm(canvas)
    assert ppm.split("\n")[:3] == ["P3", "5 3", "255"]


def test_constructing_ppm_pixel_data() -> None:
    canvas = Canvas(5, 3)
    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)
    write_pixel(canvas, 0, 0, c1)
    write_pixel(canvas, 2, 1, c2)
    write_pixel(canvas, 4, 2, c3)
    ppm = canvas_to_ppm(canvas)
    assert ppm.split("\n")[3:6] == [
        "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255",
    ]


# Scenario: Splitting long lines in PPM files
# Given c ← canvas(10, 2)
# When every pixel of c is set to color(1, 0.8, 0.6)
# And ppm ← canvas_to_ppm(c) Then lines 4-7 of ppm are
#     """
#     255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204
#     153 255 204 153 255 204 153 255 204 153 255 204 153
#     255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204
#     153 255 204 153 255 204 153 255 204 153 255 204 153
#     """


def test_splitting_long_lines_in_ppm_files() -> None:
    color = Color(1, 0.8, 0.6)
    canvas = Canvas(width=10, height=2, bg_color=color)
    ppm = canvas_to_ppm(canvas)
    assert ppm.split("\n")[3:7] == [
        "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204",
        "153 255 204 153 255 204 153 255 204 153 255 204 153",
        "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204",
        "153 255 204 153 255 204 153 255 204 153 255 204 153",
    ]

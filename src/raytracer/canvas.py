from raytracer.tuples import Color


class Canvas:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.pixels = []

        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(Color(0, 0, 0))
            self.pixels.append(row)


def write_pixel(canvas: Canvas, x: int, y: int, color: Color) -> None:
    canvas.pixels[y][x] = color


def pixel_at(canvas: Canvas, x: int, y: int) -> Color:
    return canvas.pixels[y][x]

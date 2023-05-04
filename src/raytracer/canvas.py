from raytracer.tuples import Color


class Canvas:
    def __init__(self, width: int, height: int, bg_color: Color | None = None) -> None:
        self.width = width
        self.height = height
        self.pixels = []
        if bg_color is None:
            bg_color = Color(0, 0, 0)

        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(bg_color)
            self.pixels.append(row)


def write_pixel(canvas: Canvas, x: int, y: int, color: Color) -> None:
    canvas.pixels[y][x] = color


def pixel_at(canvas: Canvas, x: int, y: int) -> Color:
    return canvas.pixels[y][x]


def canvas_to_ppm(canvas: Canvas) -> str:
    header = f"P3\n{canvas.width} {canvas.height}\n255"
    pixels = []

    for row in canvas.pixels:
        current_line = ""
        for pixel in row:
            for color_component in pixel.scaled_between(0, 255):
                component_str = str(color_component)
                if 70 - len(current_line) >= len(component_str) + 1:
                    current_line += component_str + " "
                else:
                    pixels.append(current_line.rstrip())
                    current_line = component_str + " "
        pixels.append(current_line.rstrip())

    pixel_section = "\n".join(pixels)

    ppm = "\n".join([header, pixel_section, "\n"])
    return ppm

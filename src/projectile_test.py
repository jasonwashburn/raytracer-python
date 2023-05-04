from raytracer.canvas import Canvas, canvas_to_ppm, write_pixel
from raytracer.tuples import Color, TupleFeature, Vector, normalize, point, vector


class Projectile:
    def __init__(self, position: TupleFeature, velocity: TupleFeature) -> None:
        self.position = position
        self.velocity = velocity


class Environment:
    def __init__(self, gravity: Vector, wind: Vector) -> None:
        self.gravity = gravity
        self.wind = wind


def tick(env: Environment, proj: Projectile) -> Projectile:
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position=position, velocity=velocity)


if __name__ == "__main__":
    # projectile starts one unit above the origin.
    # velocity is normalized to 1 unit/tick.
    # p ← projectile(point(0, 1, 0), normalize(vector(1, 1, 0)))
    projectile = Projectile(position=point(0, 1, 0), velocity=normalize(vector(1, 1.8, 0)) * 11.25)
    # # gravity -0.1 unit/tick, and wind is -0.01 unit/tick.
    # e ← environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))
    environment = Environment(gravity=vector(0, -0.1, 0), wind=vector(-0.01, 0, 0))

    canvas = Canvas(900, 550)

    while projectile.position.y > 0:
        x = projectile.position.x
        y = canvas.height - projectile.position.y
        write_pixel(canvas, int(x), int(y), Color(128, 128, 128))
        print(projectile.position)  # noqa
        projectile = tick(env=environment, proj=projectile)

    ppm = canvas_to_ppm(canvas)
    with open("projectile.ppm", "w") as f:
        f.write(ppm)

from raytracer.tuples import TupleFeature, Vector, normalize, point, vector


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
    projectile = Projectile(position=point(0, 1, 0), velocity=normalize(vector(1, 1, 0)))
    # # gravity -0.1 unit/tick, and wind is -0.01 unit/tick.
    # e ← environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))
    environment = Environment(gravity=vector(0, -0.1, 0), wind=vector(-0.01, 0, 0))

    while projectile.position.y > 0:
        print(projectile.position)  # noqa
        projectile = tick(env=environment, proj=projectile)

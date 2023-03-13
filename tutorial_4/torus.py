import math
import random


def is_point_in_torus(x: float, y: float, z: float, R: float, r: float) -> bool:
    return (math.sqrt(x**2 + y**2) - R) ** 2 + z**2 <= r**2


def generate_point_within_cuboid(R: float, r: float):
    x = random.uniform(-(R + r), R + r)
    y = random.uniform(-(R + r), R + r)
    z = random.uniform(-r, r)
    return (x, y, z)


def generate_a_point_within_circle(R: float):
    x = random.uniform(-R, R)
    y = random.uniform(-R, R)
    if math.sqrt(x**2 + y**2) <= R:
        return (x, y)
    else:
        return generate_a_point_within_circle(R)


def generate_point_within_cylinder(R: float, r: float):
    x, y = generate_a_point_within_circle(R + r)
    z = random.uniform(-r, r)
    return (x, y, z)


def torus_volume_cuboid(R: float, r: float, N: int = 100_000):
    """by generating N points within a cuboid, estimate the volume of a torus

    Args:
        R (float): outer radius of torus
        r (float): inner radius of torus
        N (int, optional): number of points to generate. Defaults to 100_000.
    """
    volume_of_cuboid = 8 * (R + r) ** 2 * r
    results = [is_point_in_torus(*generate_point_within_cuboid(R, r), R, r) for _ in range(N)]
    prob = sum(results) / N
    return volume_of_cuboid * prob


def torus_volume_cylinder(R, r, N=100_000):
    """by generating N points within a cylinder, estimate the volume of a torus

    Args:
        R (float): outer radius of torus
        r (float): inner radius of torus
        N (int, optional): number of points to generate. Defaults to 100_000.
    """
    volume_of_cylinder = 2 * math.pi * (R + r) ** 2 * r
    results = [is_point_in_torus(*generate_point_within_cylinder(R, r), R, r) for _ in range(N)]
    prob = sum(results) / N
    return volume_of_cylinder * prob

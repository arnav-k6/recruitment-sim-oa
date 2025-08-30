import numpy as np

def final_disk_speed(height: float, length: float, incline: float, mass: float, friction: float, radius: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.
    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """
    # Formula used: GPE1 + KE1 + RotationalKE1 = GPE2 + KE1 + RotationalKE2
    # mgh + 0 + 0 = 0 + 1/2*mv^2 + 1/2*I*w^2
    # mgh = 1/2*mv^2 + 1/2*I*w^2
    # mgh = 1/2*mv^2 + 1/4*m*r^2*(v^2/r^2)
    # mgh = 1/2*mv^2 + 1/4*m*v^2
    # mgh = 3/4*mv^2
    # gh = 3/4*v^2
    # v = sqrt(4/3*gh)
    # Note: I am assuming no slipping (only rolling through the incline), so friction is neglected.
    return math.sqrt((4/3)*9.81*height))



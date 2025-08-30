import numpy as np
import math


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
    # The final energy includes translational and rotational kinetic energy
    # E_final = 1/2 * m * v^2 + 1/2 * I * w^2
    # For a disk, I = 1/2 * m * r^2, and w = v/r
    # E_final = 1/2 * m * v^2 + 1/2 * (1/2 * m * r^2) * (v/r)^2
    # E_final = 1/2 * m * v^2 + 1/4 * m * v^2
    # E_final = 3/4 * m * v^2
    # v = sqrt((4/3) * E_final / m)
    gravity = 9.81
    initial_energy = mass*gravity*height
    incline_rad = math.radians(incline)
    work_by_friction = friction*mass*gravity*math.cos(incline_rad) * length

    energy_final = initial_energy - work_by_friction
    if energy_final <= 0:
        return 0.0

    return math.sqrt((4/3)*energy_final/mass)

import numpy as np
from utils import *


def move_particles(positions, velocities, radii, delta_time):
    max_x = WIDTH / PIXELS_PER_METER
    max_y = HEIGHT / PIXELS_PER_METER

    positions += velocities * delta_time

    # collision with x borders
    mask_left = positions[:, 0] - radii < 0
    mask_right = positions[:, 0] + radii > max_x
    velocities[mask_left | mask_right, 0] *= -1
    positions[mask_left, 0] = radii[mask_left]
    positions[mask_right, 0] = max_x - radii[mask_right]

    # collision with y borders
    mask_top = positions[:, 1] - radii < 0
    mask_bottom = positions[:, 1] + radii > max_y
    velocities[mask_top | mask_bottom, 1] *= -1
    positions[mask_top, 1] = radii[mask_top]
    positions[mask_bottom, 1] = max_y - radii[mask_bottom]


def detect_collisions(positions, velocities, radii, masses):
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            # Vector que une centros
            impact = positions[j] - positions[i]
            dist = np.linalg.norm(impact)
            min_dist = radii[i] + radii[j]

            if dist < min_dist:

                # push the particles out
                overlap = min_dist - dist
                direction = impact.copy()
                set_magnitude(direction, overlap * 0.5)
                positions[i] -= direction
                positions[j] += direction

                dist = min_dist
                set_magnitude(impact, dist)

                # colission resolution
                v1_new, v2_new = resolve_elastic_collision(
                    velocities[i], masses[i], velocities[j], masses[j], impact, dist
                )

                velocities[i] = v1_new
                velocities[j] = v2_new


def resolve_elastic_collision(v1, m1, v2, m2, impact, distance):
    mass_summ = m1 + m2
    vel_diff = v2 - v1

    numerator = np.dot(vel_diff, impact)
    denominator = mass_summ * distance * distance

    deltaV1 = impact.copy()
    deltaV2 = impact.copy()

    impulse1 = ((2 * m2 * numerator) / denominator) * deltaV1
    impulse2 = ((-2 * m1 * numerator) / denominator) * deltaV2

    v1_new = v1 + impulse1
    v2_new = v2 + impulse2

    return v1_new, v2_new

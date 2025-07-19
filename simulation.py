import numpy as np
import math
from utils import *


def move_particles(positions, velocities, radii, delta_time):
    """
    Mueve partículas y maneja colisiones con los bordes.
    """
    max_x = WIDTH / PIXELS_PER_METER
    max_y = HEIGHT / PIXELS_PER_METER

    # Mover todas las partículas
    positions += velocities * delta_time

    # Colisión con bordes en X
    mask_left = positions[:, 0] - radii < 0
    mask_right = positions[:, 0] + radii > max_x
    velocities[mask_left | mask_right, 0] *= -1
    positions[mask_left, 0] = radii[mask_left]
    positions[mask_right, 0] = max_x - radii[mask_right]

    # Colisión con bordes en Y
    mask_top = positions[:, 1] - radii < 0
    mask_bottom = positions[:, 1] + radii > max_y
    velocities[mask_top | mask_bottom, 1] *= -1
    positions[mask_top, 1] = radii[mask_top]
    positions[mask_bottom, 1] = max_y - radii[mask_bottom]


def detect_collisions(positions, velocities, radii, masses):
    """
    Detecta y resuelve colisiones elásticas entre partículas.
    También corrige solapamientos.
    """
    n = len(positions)

    for i in range(n):
        for j in range(i + 1, n):
            # Vector que une centros
            delta = positions[j] - positions[i]
            dist = np.linalg.norm(delta)
            min_dist = radii[i] + radii[j]

            if dist < min_dist and dist > 0:
                # Separar las partículas para evitar solapamiento
                overlap = min_dist - dist
                direction = delta / dist
                positions[i] -= direction * \
                    (overlap * masses[j] / (masses[i] + masses[j]))
                positions[j] += direction * \
                    (overlap * masses[i] / (masses[i] + masses[j]))

                # Resolver colisión elástica
                v1_new, v2_new = resolve_elastic_collision(
                    velocities[i], masses[i], velocities[j], masses[j], direction
                )

                velocities[i] = v1_new
                velocities[j] = v2_new


def resolve_elastic_collision(v1, m1, v2, m2, n_hat):
    """
    Resuelve una colisión elástica unidimensional a lo largo del eje definido por n_hat.

    Parámetros:
    - v1, v2: vectores de velocidad previos al choque
    - m1, m2: masas de las partículas
    - n_hat: vector unitario que apunta de la partícula 1 a la 2

    Retorna:
    - v1_new, v2_new: vectores de velocidad después del choque
    """
    # Velocidad relativa
    v_rel = v1 - v2
    vel_along_n = np.dot(v_rel, n_hat)

    # Si se están separando, no hay choque
    if vel_along_n >= 0:
        return v1, v2

    # Impulso escalar para choque elástico (e = 1)
    J = -2 * vel_along_n / (1/m1 + 1/m2)

    # Actualizar velocidades
    v1_new = v1 + (J / m1) * n_hat
    v2_new = v2 - (J / m2) * n_hat

    return v1_new, v2_new

# Ejemplo de uso:
# posiciones = np.array([...])  # shape (N, 2)
# velocidades = np.array([...])  # shape (N, 2)
# radios = np.array([...])
# masas = np.array([...])
# dt = 0.016  # por ejemplo
# move_particles(posiciones, velocidades, radios, dt)
# detect_collisions(posiciones, velocidades, radios, masas)

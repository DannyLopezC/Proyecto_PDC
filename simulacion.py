import math


def move_particles(particles, delta_time):
    for p in particles:
        p["pos"][0] += p["vel"][0] * delta_time
        p["pos"][1] += p["vel"][1] * delta_time


def detect_colissions(particles):
    n = len(particles)
    for i in range(n):
        for j in range(i+1, n):
            p1 = particles[i]
            p2 = particles[j]
            dx = p2["pos"][0] - p1["pos"][0]
            dy = p2["pos"][1] - p1["pos"][1]
            distance = math.hypot(dx, dy)

            if distance <= p1["radius"] + p2["radius"]:
                resolve_colissions(p1, p2)


def resolve_colissions(p1, p2):
    p1["vel"][0] *= -1
    p2["vel"][0] *= -1

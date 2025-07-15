import pygame
from utils import PIXELS_PER_METER


def draw_screen(screen, particle):
    # drawing paricles as circles with given position and radius
    for p in particle:
        x = int(p["pos"][0] * PIXELS_PER_METER)
        y = int(p["pos"][1] * PIXELS_PER_METER)
        r = int(p["radius"] * PIXELS_PER_METER)

        pygame.draw.circle(screen, p["color"], (x, y), r)

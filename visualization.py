import pygame


def draw_screen(screen, particle):
    # drawing paricles as circles with given position and radius
    for p in particle:
        pygame.draw.circle(screen, p["color"], (int(
            p["pos"][0]), int(p["pos"][1])), int(p["radius"]))

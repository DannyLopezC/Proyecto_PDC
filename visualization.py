import pygame
import numpy as np
from utils import *


def draw_screen(screen, positions, radii, show_mass, masses):
    font = pygame.font.Font(None, 24)

    for i in range(len(positions)):
        x = int(positions[i, 0] * PIXELS_PER_METER)
        y = int(positions[i, 1] * PIXELS_PER_METER)
        r = int(radii[i] * PIXELS_PER_METER)

        pygame.draw.circle(screen, (255, 0, 0), (x, y), r)

        if show_mass and masses is not None:
            mass_text = font.render(f"{masses[i]:.2f} kg", True, FONT_COLOR)
            text_rect = mass_text.get_rect(center=(x, y))
            screen.blit(mass_text, text_rect)

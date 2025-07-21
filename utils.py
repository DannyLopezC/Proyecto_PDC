import numpy as np

# physics constants
PIXELS_PER_METER = 100
GRAVITY = 9.81

# rendering constants
FONT_COLOR = (255, 255, 255)  # white
FONT_SIZE = 20

WIDTH = 800
HEIGHT = 600


def set_magnitude(vec, mag):
    norm = np.linalg.norm(vec)
    if norm == 0:
        return
    vec *= mag / norm

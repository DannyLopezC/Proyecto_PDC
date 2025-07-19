import pygame
import pygame_gui
import interface_gui
import simulation
import visualization
import numpy as np
from utils import *


def run_simulation(positions, velocities, radii, masses, show_mass):
    pygame.init()
    width, height = WIDTH, HEIGHT
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Simulación")
    clock = pygame.time.Clock()

    # create button for back
    manager = pygame_gui.UIManager((width, height))
    button_back = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((10, 10), (100, 30)),
        text='Volver',
        manager=manager
    )

    running = True
    while running:
        delta_time = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # salir del todo

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_back:
                    return "Back"  # volver al menú

            manager.process_events(event)

        # physics
        simulation.move_particles(positions, velocities, radii, delta_time)
        simulation.detect_collisions(positions, velocities, radii, masses)

        # visualization
        screen.fill((0, 0, 0))
        visualization.draw_screen(screen, positions, radii, show_mass, masses)
        manager.update(delta_time)
        manager.draw_ui(screen)
        pygame.display.flip()


def main():
    prev_paricles_num = None
    prev_particles = None
    prev_show_mass = False

    while True:
        result = interface_gui.open_interface(
            prev_paricles_num, prev_particles, prev_show_mass)

        if not result:
            break

        num, positions, velocities, radii, masses, show_mass = result

        # copy of the arrays
        positions_copy = np.copy(positions)
        velocities_copy = np.copy(velocities)
        radii_copy = np.copy(radii)
        masses_copy = np.copy(masses)

        simulation_state = run_simulation(
            positions_copy, velocities_copy, radii_copy, masses_copy, show_mass)

        if simulation_state == "Back":
            # save previous data
            prev_paricles_num = num
            prev_particles = [
                {
                    "pos": positions[i].tolist(),
                    "vel": velocities[i].tolist(),
                    "radius": radii[i],
                    "mass": masses[i],
                    "color": (255, 0, 0)
                }
                for i in range(num)
            ]
            prev_show_mass = show_mass
            continue
        else:
            break

    pygame.quit()


if __name__ == "__main__":
    main()

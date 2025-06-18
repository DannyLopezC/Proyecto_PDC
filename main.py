import pygame
import interface_gui
import simulation
import visualization
import interface


def main():
    particles = interface_gui.open_interface()
    if not particles:
        return

    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    # main thread
    running = True
    while running:
        # delta time for physics
        delta_time = clock.tick(60) / 1000.0  # seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # physics
        simulation.move_particles(particles, delta_time)
        simulation.detect_colissions(particles)

        screen.fill((0, 0, 0))
        # draw particles based on particles data
        visualization.draw_screen(screen, particles)
        # change buffer
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

import pygame
from interfaz_gui import abrir_interfaz
from simulacion import move_particles, detect_colissions, resolve_colissions
from interfaz import get_users_data
from visualizacion import draw_screen


def main():
    particles = abrir_interfaz()
    if not particles:
        return

    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    delta_time = 1/60

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        move_particles(particles, delta_time)
        detect_colissions(particles)

        screen.fill((0, 0, 0))
        draw_screen(screen, particles)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

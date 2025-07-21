import pygame
import pygame_gui
import copy
import random
import numpy as np


def create_input_particles_num(manager):
    label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 20), (200, 30)),
        text="Número de partículas:", manager=manager
    )
    input_line = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((230, 20), (100, 30)),
        manager=manager
    )
    # generate button
    button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((350, 20), (140, 30)),
        text='Generar Partículas', manager=manager
    )
    return input_line, button


def crear_scroll_container(manager):
    return pygame_gui.elements.UIScrollingContainer(
        relative_rect=pygame.Rect((20, 70), (560, 550)),
        manager=manager
    )


def create_particle_panel(manager, scroll_container, index, valores_default):
    panel = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((0, index * 140), (540, 130)),
        manager=manager,
        container=scroll_container,
        starting_height=1
    )

    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((0, 0), (200, 20)),
        text=f"Partícula {index + 1}", manager=manager, container=panel
    )

    entradas = []
    campos = ['X', 'Y', 'VX', 'VY', 'Radio', 'Masa']

    for j, (campo, valor) in enumerate(zip(campos, valores_default)):
        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((10, 30 + j * 15), (60, 20)),
            text=campo, manager=manager, container=panel
        )
        entry = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((80, 30 + j * 15), (60, 20)),
            manager=manager, container=panel
        )
        entry.set_text(str(valor))
        entradas.append(entry)

    return panel, entradas


def read_particle_data(particles_panels):
    positions = []
    velocities = []
    radii = []
    masses = []

    for _, entries in particles_panels:
        try:
            values = [float(e.get_text()) for e in entries]
            positions.append([values[0], values[1]])
            velocities.append([values[2], values[3]])
            radii.append(values[4])
            masses.append(values[5])
        except:
            print("Error leyendo datos de partícula")
            return None

    return (
        np.array(positions, dtype=np.float32),
        np.array(velocities, dtype=np.float32),
        np.array(radii, dtype=np.float32),
        np.array(masses, dtype=np.float32)
    )


def open_interface(prev_particles_num=None, prev_values=None, show_mass_prev=False):
    pygame.init()
    window = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("Simulación de colisiones 2D")
    manager = pygame_gui.UIManager((600, 700))
    clock = pygame.time.Clock()

    input_num, generate_button = create_input_particles_num(manager)
    scroll_container = crear_scroll_container(manager)

    checkbox_show_mass = pygame_gui.elements.UICheckBox(
        relative_rect=pygame.Rect((20, 640), (30, 30)),
        text="Mostrar masas",
        manager=manager
    )

    particles_panels = []
    button_play = None
    result = None
    running = True
    show_mass = False
    num = prev_particles_num

    # autogeneration if there are previous data
    if prev_particles_num and prev_values:
        input_num.set_text(str(prev_particles_num))

        for panel, _ in particles_panels:
            panel.kill()
        particles_panels.clear()

        for i in range(prev_particles_num):
            p = copy.deepcopy(prev_values[i])
            pos = list(p["pos"])
            vel = list(p["vel"])
            valores_default = [
                pos[0], pos[1],
                vel[0], vel[1],
                p["radius"], p["mass"]
            ]

            panel, entradas = create_particle_panel(
                manager, scroll_container, i, valores_default)
            particles_panels.append((panel, entradas))

        scroll_container.set_scrollable_area_dimensions(
            (540, prev_particles_num * 140 + 10))

        if button_play:
            button_play.kill()
        button_play = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((200, 640), (200, 30)),
            text="Iniciar Simulación", manager=manager
        )

        if show_mass_prev:
            checkbox_show_mass._toggle_state()

    while running:

        delta_time = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == button_play:
                result = read_particle_data(particles_panels)
                if result is not None:
                    show_mass = checkbox_show_mass.is_checked
                    running = False

            # if any button pressed
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                # if generate button pressed
                if event.ui_element == generate_button:
                    # get the particle num
                    try:
                        num = int(input_num.get_text())
                    except ValueError:
                        print("Número inválido")
                        continue

                    if not (1 <= num <= 100):
                        print("Debe estar entre 1 y 100 partículas")
                        continue

                    # clean previous panels
                    for panel, _ in particles_panels:
                        panel.kill()
                    particles_panels.clear()

                    for i in range(num):
                        valores_default = [
                            round(random.uniform(1.0, 5.0), 2),   # X
                            round(random.uniform(1.0, 3.0), 2),   # Y
                            round(random.uniform(-1.0, 1.0), 2),  # VX
                            round(random.uniform(-1.0, 1.0), 2),  # VY
                            round(random.uniform(0.1, 0.2), 2),   # Radio
                            round(random.uniform(0.5, 5.0), 2)    # Masa
                        ]

                        # create panels for everty particle
                        panel, entradas = create_particle_panel(
                            manager, scroll_container, i, valores_default)
                        particles_panels.append((panel, entradas))

                    scroll_container.set_scrollable_area_dimensions(
                        (540, num * 140 + 10))

                    if button_play:
                        button_play.kill()
                    button_play = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((200, 640), (200, 30)),
                        text="Iniciar Simulación", manager=manager
                    )

                # if play simulation button pressed
                elif event.ui_element == button_play:
                    result = read_particle_data(particles_panels)
                    if result is not None:
                        running = False

            manager.process_events(event)

        manager.update(delta_time)
        window.fill((40, 40, 40))
        manager.draw_ui(window)
        pygame.display.flip()

    pygame.quit()
    if result is None:
        return None

    positions, velocities, radii, masses = result
    return num, positions, velocities, radii, masses, show_mass

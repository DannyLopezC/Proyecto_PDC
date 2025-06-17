import pygame
import pygame_gui


def crear_input_numero_particulas(manager):
    label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 20), (200, 30)),
        text="Número de partículas:", manager=manager
    )
    input_line = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((230, 20), (100, 30)),
        manager=manager
    )
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


def crear_panel_particula(manager, scroll_container, index, valores_default):
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


def leer_datos_particulas(particles_panels):
    resultado = []
    for _, entradas in particles_panels:
        try:
            valores = [float(e.get_text()) for e in entradas]
            p = {
                "pos": [valores[0], valores[1]],
                "vel": [valores[2], valores[3]],
                "radius": valores[4],
                "mass": valores[5],
                "color": (255, 0, 0)
            }
            resultado.append(p)
        except:
            print("Error leyendo datos de partícula")
            return None
    return resultado


def abrir_interfaz():
    pygame.init()
    window = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("Simulación de colisiones 2D")
    manager = pygame_gui.UIManager((600, 700))
    clock = pygame.time.Clock()

    input_num, generate_button = crear_input_numero_particulas(manager)
    scroll_container = crear_scroll_container(manager)

    particles_panels = []
    button_play = None
    resultado = None
    corriendo = True

    while corriendo:
        delta_time = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == generate_button:
                    try:
                        num = int(input_num.get_text())
                    except ValueError:
                        print("Número inválido")
                        continue

                    if not (1 <= num <= 20):
                        print("Debe estar entre 1 y 20 partículas")
                        continue

                    # Limpiar anteriores
                    for panel, _ in particles_panels:
                        panel.kill()
                    particles_panels.clear()

                    for i in range(num):
                        valores_default = [100 + i*200, 100,
                                           50 if i <= 0 else -50, 0, 20, 1]
                        panel, entradas = crear_panel_particula(
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

                elif event.ui_element == button_play:
                    resultado = leer_datos_particulas(particles_panels)
                    if resultado is not None:
                        corriendo = False

            manager.process_events(event)

        manager.update(delta_time)
        window.fill((40, 40, 40))
        manager.draw_ui(window)
        pygame.display.flip()

    pygame.quit()
    return resultado

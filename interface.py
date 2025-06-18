# this was to get the data by console, currently decaprecated

def get_users_data():
    n = int(input("¿Cuántas partículas quieres simular? "))
    particles = []
    for i in range(n):
        x = float(input(f"Partícula {i+1} - posición X: "))
        y = float(input(f"Partícula {i+1} - posición Y: "))
        vx = float(input(f"Partícula {i+1} - velocidad X: "))
        vy = float(input(f"Partícula {i+1} - velocidad Y: "))
        r = float(input(f"Partícula {i+1} - radio: "))
        m = float(input(f"Partícula {i+1} - masa: "))

        particle = {
            "pos": [x, y],
            "vel": [vx, vy],
            "radius": r,
            "mass": m,
            "color": (255, 0, 0)
        }
        particles.append(particle)

    return particles

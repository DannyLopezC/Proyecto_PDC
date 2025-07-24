# 🧪 Simulador de Colisiones 2D con Python

Este proyecto es un simulador interactivo que representa colisiones entre partículas en dos dimensiones usando física clásica. Está diseñado con fines educativos, para facilitar la comprensión de conceptos como momento, masa, velocidad y colisión elástica.

---

## 🎯 Objetivo del Proyecto

Crear una herramienta visual que permita:

- Configurar partículas (posición, masa, velocidad y color).
- Simular sus movimientos y colisiones.
- Visualizar los resultados usando la biblioteca gráfica `pygame`.

---

## 📌 Características

- Soporte para múltiples partículas.
- Visualización del movimiento en tiempo real.
- Cálculo de colisiones elásticas basado en masa y dirección.
- Interfaz gráfica con `pygame_gui` para cambiar parámetros.

---

## 🖼️ Vista previa

![Diagrama de flujo](https://github.com/DannyLopezC/Proyecto_PDC/blob/main/diagrams/mainDiagram.drawio.png)

---

## 🔧 Requisitos

Este proyecto requiere Python 3.8 o superior. Las dependencias necesarias son:

```bash
pip install pygame-ce pygame_gui numpy
```

🔴 Si se tiene la libreria de pygame instalada deberá desinstalar pygame y pygame-ce para despues volver a instalar pygame-ce para evitar conflictos.

```bash
pip uninstall pygame-ce pygame
```

```bash
pip install pygame-ce
```

---

## ▶️ Cómo ejecutar el proyecto

1. Clona este repositorio:

   ```bash
   git clone https://github.com/DannyLopezC/Proyecto_PDC.git
   cd Proyecto_PDC
   ```

2. Ejecuta el archivo principal:

   ```bash
   python main.py
   ```

   Esto abrirá la ventana del simulador con las partículas en movimiento.

---

## 📁 Estructura del proyecto

```
Proyecto_PDC/
├── main.py               # Script principal
├── simulation.py         # Lógica física de colisiones y movimiento
├── visualization.py      # Dibujado de partículas en pantalla
├── interface_gui.py      # Interfaz con pygame_gui
├── interface.py          # Parametros por consola, obsoleto actualmente
├── utils.py              # Constantes y funciones auxiliares
└── README.md             # Este archivo
```

---

## 🧠 Conceptos utilizados

- Cinemática 2D
- Conservación de momento lineal
- Colisiones elásticas
- Vectores con `numpy`

---

## 📸 Ejemplo visual

![Simulación](https://github.com/DannyLopezC/Proyecto_PDC/blob/main/example.gif)

---

## 📚 Créditos

Proyecto desarrollado como alternativa de programación final para la asignatura **Programación de Computadores** en la Universidad Nacional de Colombia.

Autor: [DannyLopezC](https://github.com/DannyLopezC)

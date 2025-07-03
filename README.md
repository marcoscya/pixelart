# 🟡 Pacman Pixel Art Animado - Mascota de Escritorio

Este proyecto consiste en una animación de Pacman en estilo **pixel art**, integrada como una especie de **mascota virtual** que se mueve libremente por el escritorio de Windows.

---

## 🛠️ Herramientas Utilizadas

- 🎨 **Piskel**: Editor de pixel art usado para crear y exportar los sprites.
- 🐍 **Python + Pygame**: Para la lógica de animación y renderizado.
- 🪟 **pywin32**: Para manipular la ventana y permitir que se muestre sin bordes ni fondo (transparente).

---

---

## ⚙️ Instalación y requisitos

### 📋 Requisitos previos

- Tener **Python 3.8 o superior** instalado
- Usar **Windows** (por el uso de `pywin32`)
- Tener **pip** actualizado

### 🔧 Instalación de dependencias

Ejecuta estos comandos en tu terminal (uno por uno):

```bash
pip install pygame
pip install pywin32
```

---

## 🎬 Animación, Movimiento y Comportamiento

- El sprite sheet contiene **87 frames** en una grilla de **11 columnas x 8 filas**.
- Inicialmente solo se mostraban **11 frames** debido a que el código solo leía una fila horizontal.
- ✅ Se corrigió el método `cargar_frames()` para recorrer correctamente todas las filas y columnas del sprite sheet.
- Se implementó una animación en bucle, que reproduce continuamente los 87 frames.

---

## 🎯 Mejoras Técnicas Realizadas

### ✔️ Movimiento libre con mouse
- Se puede **arrastrar el personaje con el mouse** por cualquier parte del escritorio.

### ✔️ Eliminación de rebotes bruscos
- Se corrigió el comportamiento de retroceso que presentaba la animación al llegar al borde.

### ✔️ Transparencia real
- Gracias a `pywin32`, la ventana de Pygame se volvió:
  - **Transparente** (sin fondo visible).
  - **Sin bordes** (`NOFRAME`).
  - **Topmost**, es decir, siempre encima del escritorio.

### ✔️ Ocupación de toda la pantalla
- Se detectó que el personaje desaparecía en ciertas zonas porque la ventana tenía tamaño limitado (`800x600`).
- Se reemplazó por:
  ```python
  ANCHO, ALTO = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

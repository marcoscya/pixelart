import pygame as pg

class Character:
    def __init__(self, ruta_sprite, ancho, alto, fps=20):
        self.sprite_sheet = pg.image.load(ruta_sprite).convert_alpha()
        self.ancho = ancho
        self.alto = alto
        self.fps = fps
        self.frames = self.cargar_frames()
        self.frame_actual = 0
        self.tiempo_acumulado = 0
        self.x = 100
        self.y = 200
        self.velocidad = 2
    
    def cargar_frames(self):
        frames = []
        columnas = 11
        filas = 8
        total_frames = 87

        for fila in range(filas):
            for columna in range(columnas):
                if len(frames) >= total_frames:
                    break
                x = columna * self.ancho
                y = fila * self.alto
                frame = self.sprite_sheet.subsurface((x, y, self.ancho, self.alto))
                frames.append(frame)

        print(f"Frames cargados: {len(frames)}")  # ✅ Debería mostrar 87
        return frames
    
    def actualizar(self, delta_time):
        # Solo animación (sin mover posición)
        self.tiempo_acumulado += delta_time
        if self.frame_actual < len(self.frames) - 1:
            if self.tiempo_acumulado >= 1000 / self.fps:
                self.frame_actual += 1
                self.tiempo_acumulado = 0

        
    def dibujar(self, pantalla):
        frame = self.frames[self.frame_actual]
        frame_escalado = pg.transform.scale(frame, 
            (self.ancho * 2, self.alto * 2))
        pantalla.blit(frame_escalado, (self.x, self.y))    
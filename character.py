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
        self.x = 300
        self.y = 200
        self.velocidad = 2

        self.arrastrando = False
        self.offset_x = 0
        self.offset_y = 0
    
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

        print(f"Frames cargados: {len(frames)}") 
        return frames
    
    def actualizar(self, delta_time):
        # Solo animación (sin mover posición)
        self.tiempo_acumulado += delta_time
        if self.tiempo_acumulado >= 1000 / self.fps:
            self.frame_actual = (self.frame_actual + 1) % len(self.frames)
            self.tiempo_acumulado = 0

        
    def dibujar(self, pantalla):
        frame = self.frames[self.frame_actual]
        frame_escalado = pg.transform.scale(frame, 
            (self.ancho * 2, self.alto * 2))
        pantalla.blit(frame_escalado, (self.x, self.y))

    def mover(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if self.x <= mouse_x <= self.x + self.ancho * 2 and self.y <= mouse_y <= self.y + self.alto * 2:
                self.arrastrando = True
                self.offset_x = mouse_x - self.x
                self.offset_y = mouse_y - self.y
            
        elif event.type == pg.MOUSEBUTTONUP:
                self.arrastrando = False
            
        elif event.type == pg.MOUSEMOTION and self.arrastrando:
                mouse_x, mouse_y = event.pos
                self.x = mouse_x - self.offset_x
                self.y = mouse_y - self.offset_y
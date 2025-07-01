import pygame as pg

class Character:
    def __init__(self, ruta_sprite, ancho, alto, fps=10):
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
        sheet_width = self.sprite_sheet.get_width()
        total_frames = sheet_width // self.ancho
        return [self.sprite_sheet.subsurface((
            i * self.ancho, 0, self.ancho, self.alto
        ))
        for i in range(total_frames)        
        ]
    
    def actualizar(self, delta_time):

        # Movimiento horizontal
        self.x += self.velocidad
        if self.x < 0 or self.x + self.ancho > 800:
            self.velocidad *= -1

        # Animacion cambio de cuadrado
        self.tiempo_acumulado += delta_time
        if self.tiempo_acumulado >= 1000 / self.fps:
            self.frame_actual = (self.frame_actual + 1) % len(self.frames)
            self.tiempo_acumulado = 0
        
    def dibujar(self, pantalla):
        frame = self.frames[self.frame_actual]
        frame_escalado = pg.transform.scale(frame, 
            (self.ancho * 2, self.alto * 2))
        pantalla.blit(frame_escalado, (self.x, self.y))    
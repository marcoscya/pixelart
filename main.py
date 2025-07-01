import pygame as pg
from character import Character
from config import *

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
pg.display.set_caption("Pacman Pixel Art")

character = Character("assets/pacman.png", 90, 116)

clock = pg.time.Clock()
running = True

while running:
    delta_time = clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pantalla.fill((30, 30, 30))
    character.actualizar(delta_time)
    character.dibujar(pantalla)
    pg.display.update()

pg.quit()
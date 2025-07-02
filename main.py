import pygame as pg
import ctypes
import win32gui
import win32con
import win32api


from character import Character
from config import *

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO), pg.NOFRAME)
pg.display.set_caption("Pacman Pixel Art")

hwnd = pg.display.get_wm_info()['window']

win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 100, 100, 0, 0,
                        win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE)
extended_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)

win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                        extended_style | win32con.WS_EX_LAYERED)

win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(30, 30, 30), 0,
                                    win32con.LWA_COLORKEY)

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
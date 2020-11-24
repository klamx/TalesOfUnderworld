import pygame
from lib import *

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fin = False
    reloj = pygame.time.Clock()

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        pygame.display.flip()
        reloj.tick(30)

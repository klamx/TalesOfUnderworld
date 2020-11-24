import pygame

# Constantes
ANCHO = 800
ALTO = 600

# sabana de sprites, cantidad de sprites en x, cantidad de sprites en y
def recortar(sheet, cx, cy):
    imagen = pygame.image.load(sheet)
    info = imagen.get_rect()
    an_img = info[2]
    al_img = info[3]
    px = an_img / cx
    py = al_img / cy

    m = []
    for j in range(cy):
        fila = []
        for c in range(cx):
            cuadro = imagen.subsurface(px*c, py*j, px, py)
            fila.append(cuadro)
        m.append(fila)
    
    return m
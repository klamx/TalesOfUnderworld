import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos, m):
        pygame.sprite.Sprite.__init__(self)
        self.m = m
        self.con = 0
        self.accion = 1
        self.lim = {0: 3, 1: 3, 2: 2, 3: 4, 6: 4, 7: 4, 8: 6, 9: 0}
        self.image = self.m[self.accion][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.salud = 300
        self.tg = 0


    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.image = self.m[self.accion][self.con]
        if self.con < self.lim[self.accion]:
            self.con += 1
        else:
            self.con = 0
            self.accion = 1
            self.tg = 0
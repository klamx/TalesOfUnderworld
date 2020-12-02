import pygame
import random
from src.lib import VERDE, ANCHO, ALTO

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, pos, sheet):
        pygame.sprite.Sprite.__init__(self)
        self.con = 9
        self.dir = 4
        self.sheet = sheet
        # self.image = self.m[self.dir][self.con]
        # self.image = pygame.Surface([40, 40])
        self.con = 0
        self.action = 0
        self.image = self.sheet[self.action][self.con]
        # self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.health = 100
        self.blocks = []
        self.q = {'0': 2, '1': 2, '2': 2, '3': 0}
        self.tmp = random.randrange(50, 250)
        self.liveTime = 1000
        self.dmg = 25
        self.dirTmp = 200


    def update(self):
        '''self.rect.x += self.velx
        self.rect.y += self.vely
        self.image = self.m[self.dir][self.con]
        if self.velx != 0 or self.vely != 0:
            if self.con < 11:
                self.con += 1
            else:
                self.con = 9 '''
        self.liveTime -= 5
        
        ls_obj = pygame.sprite.spritecollide(self, self.blocks, False)
        for b in ls_obj:
            self.q['3'] = 1
            if self.rect.right > b.rect.left and self.velx > 0:
                self.rect.right = b.rect.left
                self.velx = 0
                self.q['1'] = 1

            if self.rect.left < b.rect.right and self.velx < 0:
                self.rect.left = b.rect.right
                self.velx = 0
                self.q['1'] = 1

            if self.rect.top < b.rect.bottom and self.vely < 0:
                self.rect.top = b.rect.bottom
                self.vely = 0
                self.q['2'] = 1

            if self.rect.bottom > b.rect.top and self.vely > 0:
                self.rect.bottom = b.rect.top
                self.vely = 0
                self.q['2'] = 1

        if self.rect.right > ANCHO:
            self.q['3'] = 1
            self.rect.right = ANCHO
            self.velx = 0
            self.q['1'] = 1

        if self.rect.x < 0:
            self.q['3'] = 1
            self.rect.x = 0
            self.velx = 0
            self.q['1'] = 1

        if self.rect.bottom > ALTO:
            self.q['3'] = 1
            self.rect.bottom = ALTO
            self.vely = 0
            self.q['2'] = 1
        
        if self.rect.top < 0:
            self.q['3'] = 1
            self.rect.top = 0
            self.vely = 0
            self.q['2'] = 1
        
        # Activar estado de colision
        #if self.q['3'] == 1:
        if self.q['3'] == 1 or self.dirTmp == 0:
            moneda = random.randrange(100)
            if moneda > 50:
                self.q['1'] = 0
                moneda2 = random.randrange(100)
                if moneda2 > 50:
                    self.velx = 5
                else:
                    self.velx = -5
            else:
                self.q['2'] = 0
                moneda2 = random.randrange(100)
                if moneda2 > 50:
                    self.vely = 5
                else:
                    self.vely = -5

            #self.q['3'] = 0
            self.dirTmp = 200

        if self.velx == 5:
            self.action = 3
        if self.velx == -5:
            self.action = 2
        if self.vely == 5:
            self.action = 0
        if self.vely == -5:
            self.action = 4
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.image = self.sheet[self.action][self.con]
        if self.con < 4:
            self.con += 1
        else:
            self.con = 0

        self.dirTmp -= 1
import pygame
import random

class Generator(pygame.sprite.Sprite):
    def __init__(self, pos, sheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = sheet
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.tmp = random.randrange(50, 250)
        self.velx = 0
        self.vely = 0
        self.healthMax = 800
        self.health = 800

    def update(self):
        self.tmp -= 1
        self.rect.x += self.velx
        self.rect.y += self.vely
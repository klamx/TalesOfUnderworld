import pygame
from lib import BLANCO

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, propor = [100, 100]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(propor)
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
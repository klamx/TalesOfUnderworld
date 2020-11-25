import pygame

class Key(pygame.sprite.Sprite):
    def __init__(self, pos, sheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = sheet
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

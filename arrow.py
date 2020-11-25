import pygame

class Arrow(pygame.sprite.Sprite):
	def __init__(self, pos, sheet):
		pygame.sprite.Sprite.__init__(self)
		self.image = sheet;
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]

	def update(self):
		self.rect.x = self.rect.x
		self.rect.y = self.rect.y
import pygame

class Male(pygame.sprite.Sprite):
    def __init__(self, pos, sheet):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = sheet
        self.con = 0
        self.action = 3
        self.last = 3
        # [0-3]: idle up, left, down, rigth
        # [4-7]: lance hits up, left, down, rigth
        # [8-11]: movements up, left, down, rigth
        # [12-15]: dagger hits up, left, down, rigth
        # [20]: death
        self.lim = {0: 6, 1: 6, 2: 6, 3: 6,
                    4: 8, 5: 8, 6: 8, 7: 8,
                    8: 8, 9: 8, 10: 8, 11: 8,
                    12: 5, 13: 5, 14: 5, 15: 5,
                    20: 6}
        self.image = self.sheet[self.action][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.health = 300
        self.lives = 3
        self.hit_type = 0
        self.blocks = []
        self.collide = False


    def update(self):
        #collides
        ls_obj = pygame.sprite.spritecollide(self, self.blocks, False)

        for b in ls_obj:
            if self.rect.right > b.rect.left and self.velx > 0:
                self.rect.right = b.rect.left
                self.velx = 0
            if self.rect.left < b.rect.right and self.velx < 0:
                self.rect.left = b.rect.right
                self.velx = 0
            if self.rect.bottom > b.rect.top and self.vely > 0:
                self.rect.bottom = b.rect.top
                self.vely = 0
            if self.rect.top < b.rect.bottom and self.vely < 0:
                self.rect.top = b.rect.bottom
                self.vely = 0
        
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.image = self.sheet[self.action][self.con]

        # Moves
        if self.velx != 0 or self.vely != 0:
            if self.con < 8:
                self.con += 1
            else:
                self.con = 0 

        # Actions
        if self.health <= 0 and self.lives >= 0:
            self.rect.x = 300
            self.rect.y = 100
            self.lives -= 1
            self.health = 300       

        if self.velx == 0 and self.vely == 0 and self.collide == False:
            if self.con < self.lim[self.action]:
                self.con += 1
            else:
                self.con = 0
                self.tg = 0
                if self.last >= 0  and self.last < 4:
                    self.action = self.last
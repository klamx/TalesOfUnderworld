import pygame
from male import Male
from blocks import Block
from lib import *

def death(male, player, mapLevel):
    pantalla.fill(NEGRO)
    pantalla.blit(mapLevel, [0, 0])
    pantalla.blit(male[20][0], [player.rect.x, player.rect.y])
    pantalla.fill(NEGRO)
    pantalla.blit(mapLevel, [0, 0])
    pantalla.blit(male[20][1], [player.rect.x, player.rect.y])
    pantalla.fill(NEGRO)
    pantalla.blit(mapLevel, [0, 0])
    pantalla.blit(male[20][2], [player.rect.x, player.rect.y])
    pantalla.fill(NEGRO)
    pantalla.blit(mapLevel, [0, 0])
    pantalla.blit(male[20][3], [player.rect.x, player.rect.y])
    pantalla.fill(NEGRO)
    pantalla.blit(mapLevel, [0, 0])
    pantalla.blit(male[20][4], [player.rect.x, player.rect.y])
    pantalla.fill(NEGRO)
    pantalla.blit(mapLevel, [0, 0])
    pantalla.blit(male[20][5], [player.rect.x, player.rect.y])

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fin = False
    reloj = pygame.time.Clock()

    # Imagenes
    mapLevel = pygame.image.load('Underworld.png')
    infoMapLevel = mapLevel.get_rect()
    mapWidth = infoMapLevel[2]
    mapHeight = infoMapLevel[3]
    mapx = 0
    mapy = 0
    mapVelx = 0
    mapvely = 0
    rigthLim = 600
    leftLim = 300
    upLim = 100
    downLim = 400

    male = recortar('male.png', 13, 21)
    h = pygame.image.load('Heart.png')

    # Groups
    players = pygame.sprite.Group()
    blocks = pygame.sprite.Group()

    # Objects
    player = Male([64, 64], male)
    players.add(player)

    b = Block([0, 0], [3200, 64])
    blocks.add(b)
    b1 = Block([0, 0], [64, 1750])
    blocks.add(b1)
    b2 = Block([3125, 5], [40, 1750])
    blocks.add(b2)
    b3 = Block([5, 1720], [3170, 40])
    blocks.add(b3)
    b4 = Block([1408, 5], [64, 565])
    blocks.add(b4)
    b5 = Block([5, 290], [500, 64])
    blocks.add(b5)
    b5_2 = Block([450, 290], [64, 280])
    blocks.add(b5_2)
    b5_3 = Block([450, 510], [825, 64])
    blocks.add(b5_3)
    b6 = Block([5, 870], [500, 64])
    blocks.add(b6)
    b6_2 = Block([450, 722], [64, 200])
    blocks.add(b6_2)
    b6_3 = Block([450, 722], [825, 64])
    blocks.add(b6_3)
    b6_4 = Block([1215, 722], [64, 320])
    blocks.add(b6_4)
    b6_5 = Block([770, 1010], [510, 64])
    blocks.add(b6_5)
    b6_6 = Block([770, 1010], [64, 575])
    blocks.add(b6_6)
    b6_7 = Block([195, 1300], [575, 64])
    blocks.add(b6_7)
    b7 = Block([1090, 1300], [64, 450])
    blocks.add(b7)
    b8 = Block([1350, 1300], [630, 64])
    blocks.add(b8)
    b8_2 = Block([1663, 1300], [64, 450])
    blocks.add(b8_2)
    b9 = Block([1730, 290], [64, 790])
    blocks.add(b9)
    b9_2 = Block([1730, 290], [1085, 64])
    blocks.add(b9_2)
    b9_3 = Block([2750, 290], [64, 1070])
    blocks.add(b9_3)
    b9_4 = Block([2435, 1080], [185, 64])
    blocks.add(b9_4)
    b9_5 = Block([2435, 1080], [64, 285])
    blocks.add(b9_5)
    b9_6 = Block([2435, 1300], [750, 64])
    blocks.add(b9_6)
    b10 = Block([2175, 795], [385, 64])
    blocks.add(b10)
    b10_2 = Block([2175, 795], [64, 960])
    blocks.add(b10_2)

    player.blocks = blocks

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            # Actions
            if event.type == pygame.KEYDOWN:
                # Movements
                if event.key == pygame.K_UP:
                    player.action = 8
                    player.velx = 0
                    player.vely = -5
                    player.last = 0

                if event.key == pygame.K_LEFT:
                    player.action = 9
                    player.velx = -5
                    player.vely = 0
                    player.last = 1

                if event.key == pygame.K_DOWN:
                    player.action = 10
                    player.velx = 0
                    player.vely = 5
                    player.last = 2

                if event.key == pygame.K_RIGHT:
                    player.action = 11
                    player.velx = 5
                    player.vely = 0
                    player.last = 3

                # Hits
                # Soft hit
                if event.key == pygame.K_a:
                    if player.last == 0:
                        player.action = 12
                        player.con = 0

                    if player.last == 1:
                        player.action = 13
                        player.con = 0

                    if player.last == 2:
                        player.action = 14
                        player.con = 0

                    if player.last == 3:
                        player.action = 15
                        player.con = 0

                # Hard hit
                if event.key == pygame.K_s:
                    if player.last == 0:
                        player.action = 4
                        player.con = 0

                    if player.last == 1:
                        player.action = 5
                        player.con = 0

                    if player.last == 2:
                        player.action = 6
                        player.con = 0

                    if player.last == 3:
                        player.action = 7
                        player.con = 0

            if event.type == pygame.KEYUP:
                player.action = player.last
                player.con = 0
                player.velx = 0
                player.vely = 0
                mapVelx = 0
                mapvely = 0
                for b in blocks:
                    b.velx = 0
                    b.vely = 0

        # Map collides
        if player.rect.right > rigthLim:
            player.rect.right = rigthLim
            # player.velx = 0
            player.collide = True
            mapVelx = player.velx * -1
            for b in blocks:
                b.velx = player.velx * -1
        else:
            player.collide = False

        if player.rect.left < leftLim:
            player.rect.left = leftLim
            # player.velx = 0
            player.collide = True
            mapVelx = player.velx * -1
            for b in blocks:
                b.velx = player.velx * -1
        else:
            player.collide = False

        if player.rect.top < upLim:
            player.rect.top = upLim
            # player.vely = 0
            player.collide = True
            mapvely = player.vely * -1
            for b in blocks:
                b.vely = player.vely * -1
        else:
            player.collide = False

        if player.rect.bottom > downLim:
            player.rect.bottom = downLim
            # player.vely = 0
            player.collide = True
            mapvely = player.vely * -1
            for b in blocks:
                b.vely = player.vely * -1
        else:
            player.collide = False

        '''if mapx == 0 and player.velx == -5:
            mapVelx = 0
        
        if mapy == 0 and player.vely == -5:
            mapvely = 0'''


        if player.lives > 0:
            # Updates
            players.update()
            blocks.update()
            # Draw
            pantalla.fill(NEGRO)
            pantalla.blit(mapLevel, [mapx, mapy])
            blocks.draw(pantalla)
            players.draw(pantalla)

            if player.lives == 3:
                pantalla.blit(male[20][0], [0, 0])
                pantalla.blit(male[20][0], [64, 0])
                pantalla.blit(male[20][0], [128, 0])
                pygame.draw.line(pantalla, ROJO, [192, 32], [192 + player.health, 32], 10)
            if player.lives == 2:
                pantalla.blit(male[20][0], [0, 0])
                pantalla.blit(male[20][0], [64, 0])
                pygame.draw.line(pantalla, ROJO, [192, 32], [192 + player.health, 32], 10)
            if player.lives == 1:
                pantalla.blit(male[20][0], [0, 0])
                pygame.draw.line(pantalla, ROJO, [192, 32], [192 + player.health, 32], 10)

        else:
            death(male, player, mapLevel)

        pygame.display.flip()
        reloj.tick(15)
        mapx += mapVelx
        mapy += mapvely
        # player.health -= 5
        # print player.lives, player.health
        # print player.rect.x, player.rect.y

    pygame.quit()
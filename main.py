import pygame
from male import Male
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

    male = recortar('male.png', 13, 21)
    h = pygame.image.load('Heart.png')

    # Groups
    players = pygame.sprite.Group()
    hearts = pygame.sprite.Group()

    # Objects
    player = Male([64, 64], male)
    players.add(player)

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

        if player.lives > 0:
            # Updates
            players.update()
            # Draw
            pantalla.fill(NEGRO)
            pantalla.blit(mapLevel, [0, 0])
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
            if player.lives == 0:
                pass
        else:
            death(male, player, mapLevel)

        hearts.draw(pantalla)
        pygame.display.flip()
        reloj.tick(15)
        player.health -= 5
        print player.lives, player.health

    pygame.quit()
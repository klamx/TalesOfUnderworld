import pygame
import random
from src.male import Male
from src.blocks import Block
from src.key import Key
from src.arrow import Arrow
from src.generator import Generator
from src.generator2 import Generator2
from src.door import Door
from src.enemy2 import Enemy2
from src.trooper import Trooper
from src.lib import *

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
    start = False
    iWon = False
    reloj = pygame.time.Clock()

    # Presentation
    startBackGround = pygame.image.load('img/start.png')
    arrow = pygame.image.load('img/arrow.png')

    arrows = pygame.sprite.Group()
    arr = Arrow([330, 460], arrow)
    arrows.add(arr)

    startMusic = pygame.mixer.Sound('sound/start.ogg')
    startMusic.set_volume(0.2)
    startMusic.play()

    while not fin and not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    arr.rect.y = 530

                if event.key == pygame.K_UP:
                    arr.rect.y = 460

                if arr.rect.y == 460 and event.key == pygame.K_RETURN:
                    start = True
                    arrows.remove(arr)

                if arr.rect.y == 530 and event.key == pygame.K_RETURN:
                    start = True
                    fin = True
        
        pantalla.fill(NEGRO)
        pantalla.blit(startBackGround, [0, 0])
        arrows.update()
        arrows.draw(pantalla)
        pygame.display.flip()
    
    startMusic.stop()

    # Imagenes
    mapLevel = pygame.image.load('img/Underworld.png')
    infoMapLevel = mapLevel.get_rect()
    mapWidth = infoMapLevel[2]
    mapHeight = infoMapLevel[3]
    mapx = 0
    mapy = 0
    mapVelx = 0
    mapvely = 0
    rightLim = 600
    leftLim = 300
    upLim = 100
    downLim = 400

    nums = pygame.font.Font(None, 38)
    male = recortar('img/male.png', 13, 21)
    h = pygame.image.load('img/Heart.png')
    key = pygame.image.load('img/key.png')
    keyi = pygame.image.load('img/keyi.png')
    gen1 = pygame.image.load('img/gen1.png')
    gen2 = pygame.image.load('img/gen2.png')
    win = pygame.image.load('img/win.png')
    winner = pygame.image.load('img/winner.png')
    enem1 = recortar('img/trooper.png', 12, 17)
    bat = recortar('img/bat.png', 5, 14)

    # Groups
    players = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    keys = pygame.sprite.Group()
    generators = pygame.sprite.Group()
    generators2 = pygame.sprite.Group()
    doors = pygame.sprite.Group()
    enemys1 = pygame.sprite.Group()
    enemys2 = pygame.sprite.Group()

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

    # Keys
    k1 = Key([128, 256], key)
    keys.add(k1)
    k2 = Key([3008, 201], key)
    keys.add(k2)
    k3 = Key([2688, 1088], key)
    keys.add(k3)
    k4 = Key([2048, 1408], key)
    keys.add(k4)
    k5 = Key([1472, 1408], key)
    keys.add(k5)
    endGame = False

    # Generators
    g1 = Generator([1344, 70], gen1)
    generators.add(g1)
    g2 = Generator2([704, 1226], gen2)
    generators.add(g2)
    g3 = Generator([64, 798], gen1)
    generators.add(g3)
    g4 = Generator2([704, 1370], gen2)
    generators.add(g4)
    g5 = Generator([1150, 1660], gen1)
    generators.add(g5)
    g6 = Generator2([1728, 1660], gen2)
    generators.add(g6)
    g7 = Generator([1792, 360], gen1)
    generators.add(g7)
    g8 = Generator([2240, 864], gen1)
    generators.add(g8)
    g9 = Generator2([2500, 1150], gen2)
    generators.add(g9)
    g10 = Generator2([3070, 1230], gen2)
    generators.add(g10)

    door = Door([256, 576], win)
    doors.add(door)

    inGameMusic = pygame.mixer.Sound('sound/ingame.ogg')
    inGameMusic.set_volume(0.2)
    inGameMusic.play()

    while not fin and not endGame:
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

                '''if event.key == pygame.K_p:
                    iWon = True
                    endGame = True
                    inGameMusic.stop()'''

                # Hits
                # Soft hit
                if event.key == pygame.K_a:
                    if player.last == 0:
                        player.action = 12
                        player.con = 0
                        player.hit = player.hitType[0]
                        player.conHit += 1

                    if player.last == 1:
                        player.action = 13
                        player.con = 0
                        player.hit = player.hitType[0]
                        player.conHit += 1

                    if player.last == 2:
                        player.action = 14
                        player.con = 0
                        player.hit = player.hitType[0]
                        player.conHit += 1

                    if player.last == 3:
                        player.action = 15
                        player.con = 0
                        player.hit = player.hitType[0]
                        player.conHit += 1

                # Hard hit
                if player.conHit >= 3:
                    if event.key == pygame.K_s:
                        if player.last == 0:
                            player.action = 4
                            player.con = 0
                            player.hit = player.hitType[1]
                            player.conHit = 0

                        if player.last == 1:
                            player.action = 5
                            player.con = 0
                            player.hit = player.hitType[1]
                            player.conHit = 0

                        if player.last == 2:
                            player.action = 6
                            player.con = 0
                            player.hit = player.hitType[1]
                            player.conHit = 0

                        if player.last == 3:
                            player.action = 7
                            player.con = 0
                            player.hit = player.hitType[1]
                            player.conHit = 0

                # Take
                if event.key == pygame.K_d:
                    player.take = True

            if event.type == pygame.KEYUP:
                player.action = player.last
                player.take = False
                player.con = 0
                player.velx = 0
                player.vely = 0
                mapVelx = 0
                mapvely = 0
                for d in doors:
                    d.velx = 0
                    d.vely = 0
                for g in generators:
                    g.velx = 0
                    g.vely = 0
                for k in keys:
                    k.velx = 0
                    k.vely = 0
                for b in blocks:
                    b.velx = 0
                    b.vely = 0
                for e2 in enemys1:
                    e2.velx = 0
                    e2.vely = 0
                

        # Map collides
        if player.rect.right > rightLim:
            player.rect.right = rightLim
            # player.velx = 0
            player.collide = True
            mapVelx = player.velx * -1
            for d in doors:
                d.velx = player.velx * -1
            for g in generators:
                g.velx = player.velx * -1
            for k in keys:
                k.velx = player.velx * -1
            for b in blocks:
                b.velx = player.velx * -1

        else:
            player.collide = False

        if player.rect.left < leftLim:
            player.rect.left = leftLim
            # player.velx = 0
            player.collide = True
            mapVelx = player.velx * -1
            for d in doors:
                d.velx = player.velx * -1
            for g in generators:
                g.velx = player.velx * -1
            for k in keys:
                k.velx = player.velx * -1
            for b in blocks:
                b.velx = player.velx * -1

        else:
            player.collide = False

        if player.rect.top < upLim:
            player.rect.top = upLim
            # player.vely = 0
            player.collide = True
            mapvely = player.vely * -1
            for d in doors:
                d.vely = player.vely * -1
            for g in generators:
                g.vely = player.vely * -1
            for k in keys:
                k.vely = player.vely * -1
            for b in blocks:
                b.vely = player.vely * -1

        else:
            player.collide = False

        if player.rect.bottom > downLim:
            player.rect.bottom = downLim
            # player.vely = 0
            player.collide = True
            mapvely = player.vely * -1
            for d in doors:
                d.vely = player.vely * -1
            for g in generators:
                g.vely = player.vely * -1
            for k in keys:
                k.vely = player.vely * -1
            for b in blocks:
                b.vely = player.vely * -1

        else:
            player.collide = False

        # Collides
        ls_keys = pygame.sprite.spritecollide(player, keys, False)
        for k in ls_keys:
            if player.take == True:
                keys.remove(k)
                player.keys += 1

        ls_gen = pygame.sprite.spritecollide(player, generators, False)
        for g in ls_gen:
            if g.healthMax == 800:
                if (player.action >= 4 and player.action < 8) or (player.action >= 12 and player.action < 16):
                    if player.hit == player.hitType[0]:
                        g.health -= player.hit
                    if player.hit == player.hitType[1]:
                        g.health -= player.hit

                if g.health <= 0:
                    generators.remove(g)

        ls_win = pygame.sprite.spritecollide(player, doors, False)
        for d in ls_win:
            if player.take == True and player.keys == 5:
                iWon = True
                endGame = True

        

        # spawn generators
        for g in generators:
            if g.healthMax == 1000:
                if g.tmp <= 0:
                    e2 = Enemy2(g.rect.center, bat)

                    dado = random.randrange(100)
                    if dado < 25:
                        e2.velx = 5
                        e2.q['0'] = 1
                        e2.q['1'] = 0
                    elif dado < 50:
                        e2.velx = -5
                        e2.q['0'] = 1
                        e2.q['1'] = 0
                    elif dado < 75:
                        e2.vely = 5
                        e2.q['0'] = 0
                        e2.q['2'] = 0
                    else:
                        e2.vely = -5
                        e2.q['0'] = 0
                        e2.q['2'] = 0

                    e2.blocks = blocks
                    enemys2.add(e2)
                    g.tmp = random.randrange(50, 250)

            if g.healthMax == 800:
                if g.tmp <= 0:
                    e1 = Trooper(g.rect.center, enem1)
                    enemys1.add(e1)
                    g.tmp = random.randrange(50, 250)
            
            # TODO: arreglar la generacion de enemigos

        ls_e2 = pygame.sprite.spritecollide(player, enemys2, False)
        for e2 in ls_e2:
            player.health -= e2.dmg
            enemys2.remove(e2)

            if e2.liveTime <= 0:
                enemys2.remove(e2)
            
        for e in enemys1:
            if e.temp_m == -10:
                e.estado = 1
                e.temp_m -= 1

        ls_e1 = pygame.sprite.spritecollide(player, enemys1, False)
        for e1 in ls_e1:
            if e1.direc_ataque == 0 or e1.direc_ataque == 5 or e1.direc_ataque == 10 or e1.direc_ataque == 13:
                player.health -= e1.dmg
            '''if e1.atk == True:
                player.health -= e1.dmg
            if e1.health <= 0:
                enemys1.remove(e1)'''


        '''if mapx == 0 and player.velx == -5:
            mapVelx = 0
        
        if mapy == 0 and player.vely == -5:
            mapvely = 0'''

        txt = nums.render('X ' + str(player.keys), True, BLANCO)

        if player.lives == 0:
            endGame = True
            inGameMusic.stop()

        if player.lives > 0:
            # Updates
            players.update()
            blocks.update()
            keys.update()
            generators.update()
            doors.update()
            enemys1.update()
            enemys2.update()
            # Draw
            pantalla.fill(NEGRO)
            blocks.draw(pantalla)
            pantalla.blit(mapLevel, [mapx, mapy])
            keys.draw(pantalla)
            generators.draw(pantalla)
            doors.draw(pantalla)
            enemys1.draw(pantalla)
            enemys2.draw(pantalla)
            players.draw(pantalla)

            pantalla.blit(keyi, [512, 10])
            pantalla.blit(txt, [580, 20])

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
        # player.health -= 50
        # print player.lives, player.health
        # print player.rect.x, player.rect.y

    gameOver = pygame.image.load('img/gameover.png')

    endMusic = pygame.mixer.Sound('sound/end.ogg')
    endMusic.set_volume(0.2)
    endMusic.play()

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            
            if event.type == pygame.KEYDOWN:
                fin = True

        pantalla.fill(NEGRO)
        if iWon == True:
            pantalla.blit(winner, [0, 0])
        else:
            pantalla.blit(gameOver, [0, 0])
        pygame.display.flip()
    
    endMusic.stop()
    pygame.mixer.quit()

    pygame.quit()
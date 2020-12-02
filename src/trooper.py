import pygame
import random
from src.lib import ANCHO, ALTO

class Trooper(pygame.sprite.Sprite):
    def __init__(self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.m = m
        self.estado = 0
        self.con_n = 0
        self.accion_n = 0
        # self.tmp = random.randrange(50, 250)
        self.atk = False
        self.dmg = 25
        self.health = 200

        self.con_a = 0
        self.accion_a = 0
        self.con_ai = 0

        self.direc_ataque = {0:[1,2,3,4], 5:[6,7,8,9], 10:[11,12], 13:[14,15,16]}
        self.lim_ataque = {4:6, 9:6, 12:10, 16:6}
        self.image = self.m[self.accion_n][self.con_n]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 1
        self.vely = 1 
        self.temp = random.randrange(30,120)
        self.temp_m = random.randrange(50,100)

    def posicion(self):
        #retorna la posicion del jugador
        p = self.rect.midtop
        return p
    
    def caminar(self):               
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.image = self.m[self.accion_n][self.con_n] 

        # Definicion del movimiento en estado natural
        if self.temp_m <= 0: 
            # Momento de pausa           
            if self.temp_m == 0:
                self.velx = 0
                self.vely = 0

            # Movimiento en estado natural 
            if self.temp_m > -10:
                self.temp_m -= 1
            else:              
                self.velx = random.randrange(-3,3)
                self.vely = random.randrange(-3,3)
                self.temp_m = random.randrange(50,100)

                # Definicion de los sprites
                if self.temp_m % 2 == 0:
                    if self.velx > 0:
                        self.accion_n =  0
                    else: 
                        self.accion_n = 5
                else:
                    if self.vely < 0:
                        self.accion_n = 10
                    else: 
                        self.accion_n = 13  
        else:
            if self.rect.right > (ANCHO-60):
                self.velx = random.randrange(-3,-1)
                self.accion_n = 5
            if self.rect.left < 20:
                self.velx = random.randrange(1,3)
                self.accion_n = 0
            if self.rect.top < 20:
                self.vely = random.randrange(1,3)
                self.accion_n = 13
            if self.rect.bottom > (ALTO-60):
                self.vely = random.randrange(-3,-1)
                self.accion_n = 10
            else:
                self.temp_m -=1

        if self.con_n < 2:
            self.con_n += 1
        else:
            self.con_n = 0

    def atacar(self,lista_accion):
        self.velx = 0
        self.vely = 0
        self.image = self.m[self.accion_a][self.con_ai] 

        largo = len(lista_accion)
        if self.con_a < largo-1:
            if self.con_a +1 == largo:
                limite_temp = self.lim_ataque[self.accion_a]
                if self.con_ai+1 < limite_temp:
                    self.con_ai+=1
                else:
                    self.con_ai = 0
                    self.con_a += 1
            else:
                if self.con_ai < 11:
                    self.con_ai+=1
                else:
                    self.con_ai=0
                    self.con_a+=1
        else:
            self.con_a = 0
            self.estado = 0     

        self.atk = False

    def update(self): 
        if self.estado == 0:
            self.caminar()
        else:
            lista_accion = self.direc_ataque[self.accion_n]
            self.accion_a = lista_accion[self.con_a]
            self.atk = True
            self.atacar(lista_accion) 
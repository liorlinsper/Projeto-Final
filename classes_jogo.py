# Bibliotecas
import pygame
import random
import os

# Variáveis
WIDTH = 600
HEIGHT = 600
BLACK = (0,0,0)

#Localização dos assets:
pasta_jogo = os.path.dirname(__file__)
pasta_imagens = os.path.join(pasta_jogo, 'img')

# CLASSES:

# Sprite do Jogador:
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(pasta_imagens, "froggy.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        # VELOCIDADE:
        self.x_speed = 0
        self.y_speed = 0 
    
    def update(self):
        self.x_speed = 0
        self.y_speed = 0 
        #COMANDOS: 
        pressionado = pygame.key.get_pressed()
        if pressionado[pygame.K_LEFT]:
            self.x_speed = -15
        if pressionado[pygame.K_RIGHT]:
            self.x_speed = 15
        if pressionado[pygame.K_UP]:
            self.y_speed = -15
        if pressionado[pygame.K_DOWN]:
            self.y_speed = 15
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed 

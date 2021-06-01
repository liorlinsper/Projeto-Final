# Bibliotecas
import pygame
import random
import os

# Variáveis
WIDTH = 700
HEIGHT = 700
BLACK = (0,0,0)
WHITE = (255,255,255)

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
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        # VELOCIDADE:
        self.x_speed = 0
        self.y_speed = 0 
    
    def hide(self):
        # esconde jogador temporariamente
        self.hidden = True 
        self.hide_timer = pygame.time.get_ticks() 
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    def update(self):
        self.x_speed = 0
        self.y_speed = 0 
        #COMANDOS: 
        pressionado = pygame.key.get_pressed()
        if pressionado[pygame.K_LEFT]:
            self.x_speed = -10
        if pressionado[pygame.K_RIGHT]:
            self.x_speed = 10
        if pressionado[pygame.K_UP]:
            self.y_speed = -10
        if pressionado[pygame.K_DOWN]:
            self.y_speed = 10
        
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

        if self.hidden: 
            self.rect.centerx = WIDTH + 100 
            self.rect.bottom = HEIGHT + 100 

        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

# INIMIGOS

class Cobra(pygame.sprite.Sprite):
    def __init__(self,imagem_cobra):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem_cobra
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .8 / 2)
        # pygame.draw.circle(self.image, BLACK, self.rect.center, self.radius)
        self.rect.y = random.randrange(100,500)
        self.rect.x = 0
        self.x_speed = random.randrange(5, 12)

    def update(self):
        self.rect.x += self.x_speed
        if self.rect.x > WIDTH:
            self.rect.y = random.randrange(100,500)
            self.rect.x = 0
            self.x_speed = random.randrange(5, 12)           


class Cachorro(pygame.sprite.Sprite):
    def __init__(self,imagem_cachorro):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem_cachorro
        self.image = pygame.transform.scale(self.image, (120, 80))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = 45
        # pygame.draw.circle(self.image, BLACK, self.rect.center, self.radius)
        self.rect.y = random.randrange(50,100)
        self.rect.x = 0
        self.x_speed = random.randrange(5,10)

    def update(self):
        self.rect.x += self.x_speed
        if self.rect.x > WIDTH:
            self.rect.y = random.randrange(100,500)
            self.rect.x = 0
            self.x_speed = random.randrange(5, 10)  

class Passaro(pygame.sprite.Sprite):
    def __init__(self,imagem_passaro):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem_passaro
        self.image = pygame.transform.scale(self.image, (120, 80))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = 40
        # pygame.draw.circle(self.image, BLACK, self.rect.center, self.radius)
        self.rect.y = random.randrange(50,100)
        self.rect.x = 0
        self.x_speed = random.randrange(10,12)

    def update(self):
        self.rect.x += self.x_speed
        if self.rect.x > WIDTH:
            self.rect.y = random.randrange(100,500)
            self.rect.x = 0
            self.x_speed = random.randrange(11, 13)  

#LIBÉLULA (PONTUAÇÃO)
class libelula(pygame.sprite.Sprite):
    def __init__(self,imagem_libelula):
        pygame.sprite.Sprite.__init__(self)
        self.image =  imagem_libelula
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (30 , 40))
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(0,600)
        self.rect.x = random.randrange(0,600)


   
# Importação das bibliotecas:
import pygame
from random import randint
import os
import classes_jogo

#Localização dos assets:
pasta_jogo = os.path.dirname(__file__)
pasta_imagens = os.path.join(pasta_jogo, 'img')

# Variáveis:

WIDTH = 600
HEIGHT = 600
FPS = 30

azul_claro = (0,255,255)


#Inicialização do jogo:
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sem Nome")

clock = pygame.time.Clock()

#Sprites:
all_sprites = pygame.sprite.Group()
JOGADOR = classes_jogo.Jogador()
all_sprites.add(JOGADOR)

# Loop Principal:
game = True

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    #draw:
    window.fill((azul_claro))
    all_sprites.draw(window)
    pygame.display.flip()

# Atualização do estado do jogo:
    pygame.display.update()
    all_sprites.update()

# Finalização:
pygame.quit()
# Importação das bibliotecas:
import pygame
import random
import os
import classes_jogo

#Localização dos assets:
pasta_jogo = os.path.dirname(__file__)
pasta_imagens = os.path.join(pasta_jogo, 'img')

# Variáveis:

WIDTH = 700
HEIGHT = 700
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
INIMIGOS = pygame.sprite.Group() 
#SPAWN DE INIMIGOS:
for n in range(5):
    Cobras = classes_jogo.Cobra()
    INIMIGOS.add(Cobras)
    all_sprites.add(Cobras)

for n in range(3):
    Cachorros = classes_jogo.Cachorro()
    INIMIGOS.add(Cachorros)
    all_sprites.add(Cachorros)

# SPAWN DE LIBELULAS
for n in range(1):
    libelulas = classes_jogo.libelula()
    all_sprites.add(libelulas)

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
    all_sprites.update()
    pygame.display.update()
    #colisão
    atinge = pygame.sprite.spritecollide(JOGADOR, INIMIGOS, False)
    if atinge:
        game = False

# Finalização:
pygame.quit()
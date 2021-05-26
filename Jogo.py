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
branco  = (255,255,255)

#Inicialização do jogo:
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sem Nome")

clock = pygame.time.Clock()

# IMAGENS
imagem_libelula = pygame.image.load(os.path.join(pasta_imagens, "libelula.png")).convert()
imagem_cachorro = pygame.image.load(os.path.join(pasta_imagens, "cachorro.png")).convert()
imagem_cobra = pygame.image.load(os.path.join(pasta_imagens, "snake.png")).convert()

#Sprites:
all_sprites = pygame.sprite.Group()
JOGADOR = classes_jogo.Jogador()
all_sprites.add(JOGADOR)
INIMIGOS = pygame.sprite.Group() 
LIBELULAS = pygame.sprite.Group()

#SPAWN DE INIMIGOS inicial:
for n in range(5):
    Cobras = classes_jogo.Cobra(imagem_cobra)
    INIMIGOS.add(Cobras)
    all_sprites.add(Cobras)

for n in range(3):
    Cachorros = classes_jogo.Cachorro(imagem_cachorro)
    INIMIGOS.add(Cachorros)
    all_sprites.add(Cachorros)

# SPAWN DE LIBELULAS
for n in range(1):
    libelulas = classes_jogo.libelula(imagem_libelula)
    LIBELULAS.add(libelulas)

# SISTEMA DE PONTOS:
score = 0

# Loop Principal:
game = True

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    #colisão
    atinge = pygame.sprite.spritecollide(JOGADOR, INIMIGOS, False, pygame.sprite.collide_circle)
    if atinge:
        game = False

    #Pontuação:
    pontos = pygame.sprite.spritecollide(JOGADOR, LIBELULAS, True)
    if len(pontos) > 0:
        score += 1
        libelulas = classes_jogo.libelula(imagem_libelula)
        LIBELULAS.add(libelulas)

    #draw:
    window.fill((branco))
    all_sprites.draw(window)
    LIBELULAS.draw(window)
    pygame.display.flip()

# Atualização do estado do jogo:
    all_sprites.update()
    LIBELULAS.update()
    pygame.display.update()







# Finalização:
pygame.quit()
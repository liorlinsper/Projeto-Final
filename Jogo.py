# Importação das bibliotecas:
import pygame
import random
import os
import classes_jogo

#Localização dos assets:
pasta_jogo = os.path.dirname(__file__)
pasta_imagens = os.path.join(pasta_jogo, 'img')
pasta_sound = os.path.join(pasta_jogo, 'sounds')


# Variáveis:

WIDTH = 700
HEIGHT = 700
FPS = 30

azul_claro = (0,255,255)
branco  = (255,255,255)
preto = (0,0,0)

#Inicialização do jogo:
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Froggy")

clock = pygame.time.Clock()


# PLACAR
fonte = pygame.font.match_font('arial')

def draw_text(surf,text,tamanho,x,y):
    fonte_ = pygame.font.Font(fonte,tamanho)
    text_surf = fonte_.render(text, True, preto)
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surf, text_rect)

#VIDAS
def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x +30 * i
        img_rect.y = y
        surf.blit(img, img_rect)


# IMAGENS
imagem_libelula = pygame.image.load(os.path.join(pasta_imagens, "libelula.png")).convert()
imagem_cachorro = pygame.image.load(os.path.join(pasta_imagens, "cachorro.png")).convert()
imagem_cobra = pygame.image.load(os.path.join(pasta_imagens, "snake.png")).convert()
imagem_passaro = pygame.image.load(os.path.join(pasta_imagens, "passaro.png")).convert()
imagem_coracao = pygame.image.load(os.path.join(pasta_imagens, "coracao.png")).convert()
imagem_coracao = pygame.transform.scale(imagem_coracao, (80, 80))
imagem_coracao.set_colorkey(preto)
background = pygame.image.load(os.path.join(pasta_imagens, "terra.png")).convert()
background2 = pygame.image.load(os.path.join(pasta_imagens, "FundoMenu.png")).convert()
background3 = pygame.image.load(os.path.join(pasta_imagens, "gameover.png")).convert()

#SONS
som_ponto = pygame.mixer.Sound(os.path.join(pasta_sound, "ponto.mp3"))
som_morte = pygame.mixer.Sound(os.path.join(pasta_sound, "morte.mp3"))

#Sprites:
all_sprites = pygame.sprite.Group()
JOGADOR = classes_jogo.Jogador()
all_sprites.add(JOGADOR)
INIMIGOS = pygame.sprite.Group() 
LIBELULAS = pygame.sprite.Group()

#SPAWN DE INIMIGOS inicial:
for n in range(4):
    Cobras = classes_jogo.Cobra(imagem_cobra)
    INIMIGOS.add(Cobras)
    all_sprites.add(Cobras)


# SPAWN DE LIBELULAS
for n in range(1):
    libelulas = classes_jogo.libelula(imagem_libelula)
    LIBELULAS.add(libelulas)

# SISTEMA DE PONTOS:
score = 0
score_anterior = 0

# Loop Principal:
menu = True
game = True
over= False
while game:
    clock.tick(FPS)
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menu = False
            
        window.fill((0,0,0))
        clock.tick(30)
        window.blit(background2,(0,0))
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    #colisão
    atinge = pygame.sprite.spritecollide(JOGADOR, INIMIGOS, False, pygame.sprite.collide_circle)
    if atinge: 
        JOGADOR.hide()
        JOGADOR.lives -= 1
        som_morte.play()

    #Se algum mob atinge o jogador
    if JOGADOR.lives <= 0:
        over = True

    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        window.fill((0,0,0))
        clock.tick(30)
        window.blit(background3,(0,0))
        pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False




    #Pontuação:
    pontos = pygame.sprite.spritecollide(JOGADOR, LIBELULAS, True)
    if len(pontos) > 0:
        score_anterior = score
        score += 1
        libelulas = classes_jogo.libelula(imagem_libelula)
        LIBELULAS.add(libelulas)
        som_ponto.play()

    # SPAWNS PARA AUMENTAR A DIFICULDADE:
        # 4 libéluas:
    if score == 4 and (score != score_anterior):
        score_anterior = score
        for n in range(2):
            Cobras = classes_jogo.Cobra(imagem_cobra)
            INIMIGOS.add(Cobras)
            all_sprites.add(Cobras)
        # 8 libéluas:
    if score == 8 and (score != score_anterior):
        score_anterior = score
        for n in range(2):
            Cachorros = classes_jogo.Cachorro(imagem_cachorro)
            INIMIGOS.add(Cachorros)
            all_sprites.add(Cachorros)
        #12 libélulas:
    if score == 12 and (score != score_anterior):
        score_anterior = score   
        for n in range(1):
            Cachorros = classes_jogo.Cachorro(imagem_cachorro)
            INIMIGOS.add(Cachorros)
            all_sprites.add(Cachorros)
        #16 libélulas:
    if score == 16 and (score != score_anterior):
        score_anterior = score
        for n in range(2):
            Cobras = classes_jogo.Cobra(imagem_cobra)
            INIMIGOS.add(Cobras)
            all_sprites.add(Cobras)
        # >= 20 libélulas:
    if score == 20 and (score != score_anterior):
        score_anterior = score
        for n in range(1):
            Passaros = classes_jogo.Passaro(imagem_passaro)
            INIMIGOS.add(Passaros)
            all_sprites.add(Passaros)    
        
        #se apertar a tecla p o jogo deve rodar a função de pausar.
    #draw:
    window.fill((branco))
    window.blit(background, (0, 0))
    all_sprites.draw(window)
    LIBELULAS.draw(window)
    pygame.display.flip()
    draw_text(window,"pontuação: {0}".format(score), 30, WIDTH/2, 10 )
    draw_lives(window , WIDTH - 250, 7, JOGADOR.lives, imagem_coracao)

# Atualização do estado do jogo:
    all_sprites.update()
    LIBELULAS.update()
    pygame.display.update()







# Finalização:
pygame.quit()
import pygame, sys
from pygame.locals import *
from random import randrange

##----------------------- CORES ----------------------------

branco = (255, 255, 255)
cinza = (128, 128, 128)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

##----------------------------------------------------------

try:
    pygame.init()
except:
    print("O módulo pygame não foi inicializado com sucesso :C ")

##------------------------- VARIÁVEIS ----------------------

largura = 900
altura = 600
tamanho = 20
placar = 40

tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption("Super Milionar.io")
relogio = pygame.time.Clock()

##-------------------------- ÁUDIO -------------------------

pygame.mixer.music.load('sound/musicafundo.mp3')

##-------------------------- IMAGENS -----------------------

moedaImg = pygame.image.load('image/moeda.png')
playerImg = pygame.image.load('image/player.png')
backgroundImg = pygame.image.load('image/background.jpg')

#----------------------------------------------------------#

def background(backx, backy):
    tela.blit(backgroundImg, pygame.Rect(backx, backy, largura, altura))

def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1, [x, y])

def player(posx, posy):
    tela.blit(playerImg, pygame.Rect(posx, posy, tamanho, tamanho))

def moeda(moedax, moeday):
    tela.blit(moedaImg, pygame.Rect(moedax, moeday, tamanho, tamanho))

def jogo():

    posx = randrange(0, largura-tamanho, 20)
    posy = randrange(0, altura-tamanho-placar, 20)

    moedax = randrange(0, largura-tamanho, 20)
    moeday = randrange(0, altura-tamanho-placar, 20)

    backx = 0
    backy = 0
    
    velocidadex = 0
    velocidadey = 0

    score = 0

    sair = False

    pygame.mixer.music.play(10)

    while sair != True:              
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

#------------------------ MOVIMENTAÇÃO --------------------#

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    sair = True
                if event.key == pygame.K_LEFT:
                    velocidadey = 0
                    velocidadex = -tamanho
                if event.key == pygame.K_RIGHT:
                    velocidadey = 0
                    velocidadex = tamanho
                if event.key == pygame.K_UP:
                    velocidadex = 0
                    velocidadey = -tamanho
                if event.key == pygame.K_DOWN:
                    velocidadex = 0
                    velocidadey = tamanho
                if event.key == pygame.K_a:
                    velocidadey = 0
                    velocidadex = -tamanho
                if event.key == pygame.K_d:
                    velocidadey = 0
                    velocidadex = tamanho
                if event.key == pygame.K_w:
                    velocidadex = 0
                    velocidadey = -tamanho
                if event.key == pygame.K_s:
                    velocidadex = 0
                    velocidadey = tamanho

#----------------------------------------------------------#

        relogio.tick(25)
        tela.fill(branco)
        posx += velocidadex
        posy += velocidadey

        if posx == moedax and posy == moeday:
            moedax = randrange(0, largura-tamanho, 20)
            moeday = randrange(0, altura-tamanho-placar, 20)
            score += 100000

        if posx + tamanho> largura:
            posx = 0
        if posx < 0:
            posx = largura - tamanho
        if posy + tamanho> altura-placar:
            posy = 0
        if posy < 0:
            posy = altura - tamanho - placar

        if score == 1100000:
            sair = True

        background(backx, backy)
        player(posx, posy)
        moeda(moedax, moeday)
                
        pygame.draw.rect(tela, preto, [0, altura-placar, largura, placar])
        texto("Score: "+str(score), branco, 20, 10, altura - 30)
        
        pygame.display.update()

jogo()

pygame.quit()

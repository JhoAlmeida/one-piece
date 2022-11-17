import pygame
import random
import time
pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("One Piece")
altura = 913
largura = 733
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
fundo = pygame.image.load("one-piece/wano.jpg")
luffy = pygame.image.load("one-piece/luffy.png")
fogo = pygame.image.load("one-piece/fogo.png")
preto = (000,000,000)
atitus = pygame.image.load("one-piece/atitus.png")



def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",20)
    textoDisplay = fonte.render(texto,True,preto)
    gameDisplay.blit(textoDisplay, (85,100))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",95)
    fonte2  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("MORREUU !!!!",True,preto)
    textoDisplay2 = fonte2.render("press enter to continue !!!!",True,preto)
    gameDisplay.blit(textoDisplay, (150,150))
    gameDisplay.blit(textoDisplay2, (150,350))
    pygameDisplay.update()

def jogar():
    jogando = True
    luffyX = 200
    luffyY = 550
    movimentoLuffyX = 0
    larguraLuffy = 300
    alturaLuffy = 396
    alturaFogo = 50
    larguraFogo = 25
    posicaoFogoX = 170
    posicaoFogoY = -200
    velocidadeFogo = 1
    pontos = 0
    pygame.mixer.music.load("one-piece/tema.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)

    fogoSound = pygame.mixer.Sound("one-piece/bola-fogo-sound.mp3")
    fogoSound.set_volume(1)
    pygame.mixer.Sound.play(fogoSound)

    explosaoSound = pygame.mixer.Sound("one-piece/aimamae.mp3")
    explosaoSound.set_volume(1)
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoLuffyX = -15
                elif event.key == pygame.K_RIGHT:
                    movimentoLuffyX = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoLuffyX = 0
            
        if jogando:
            if posicaoFogoY > altura:
                posicaoFogoY = -550
                posicaoFogoX = random.randint(0,largura)
                velocidadeFogo = velocidadeFogo + 1
                pontos = pontos + 1
                pygame.mixer.Sound.play(fogoSound)
            else:
                posicaoFogoY =posicaoFogoY + velocidadeFogo

            if luffyX + movimentoLuffyX >0 and luffyX + movimentoLuffyX< largura-larguraLuffy:
                luffyX = luffyX + movimentoLuffyX
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(luffy, (luffyX,luffyY))
            
            gameDisplay.blit(fogo, (posicaoFogoX,posicaoFogoY))
            escreverTexto("Pontos: "+str(pontos))

            pixelsXLuffy = list(range(luffyX, luffyX+larguraLuffy))
            pixelsYLuffy = list(range(luffyY, luffyY+alturaLuffy))

            pixelXFogo = list(range(posicaoFogoX, posicaoFogoX+larguraFogo))
            pixelYFogo = list(range(posicaoFogoY, posicaoFogoY+alturaFogo))

            colisaoY = len(list(set(pixelYFogo) & set(pixelsYLuffy) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXFogo) & set(pixelsXLuffy) ))
                print(colisaoX)
                if colisaoX > 45:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(explosaoSound)


        pygameDisplay.update()
        clock.tick(60)

jogar()


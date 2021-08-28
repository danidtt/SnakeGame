import pygame
import random

pygame.init()

# Dimensões de tela = 600 x 600
dimensoes = (600, 600)

# Criando janela do jogo
tela = pygame.display.set_mode(dimensoes)
pygame.display.set_caption('Snake Game')

# Cores RGB
preto = (80, 71, 70)
verde = (55, 150, 52)
vermelho = (237, 71, 74)
cinza = (192, 188, 181)

# Preencher espaço da tela com a cor atribuida
tela.fill(preto)

# Posição da cobrinha
x = 300
y = 300

# Tamanho da cobrinha
z = 20

# Lista com x e y para poder chamar os dois de uma vez
posicao = [[x, y]]

dx = 0 # Delta x
dy = 0 # Delta y

# Para a comida aparecer aleatoriamente na tela
x_comida = round(random.randrange(0, 600 - z) / 20) * 20
y_comida = round(random.randrange(0, 600 - z) / 20) * 20

# Fonte
fonte = pygame.font.SysFont('hack', 30)

## FUNÇÕES ##
def snake(posicao):
    tela.fill(preto)

    for i in posicao:                              # 20 x 20
        pygame.draw.rect(tela, vermelho, [i[0], i[1], z, z])

def mover(dx, dy, posicao):

    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                dx = -z
                dy = 0
            if i.key == pygame.K_RIGHT:
                dx = z
                dy = 0
            if i.key == pygame.K_UP:
                dx = 0
                dy = -z
            if i.key == pygame.K_DOWN:
                dx = 0
                dy = z
    
    # [x, y] = [0, 1]
    x_novo = posicao[-1][0] + dx
    y_novo = posicao[-1][1] + dy
    posicao.append([x_novo, y_novo])

    del posicao[0]

    return dx, dy, posicao

def comida(dx, dy, x_comida, y_comida, posicao):
    cabeca = posicao[-1]

    xx = cabeca[0] + dx
    yy = cabeca[1] + dy

    if cabeca[0] == x_comida and cabeca[1] == y_comida:
        posicao.append([xx, yy])

        x_comida = round(random.randrange(0, 600 - z) / 20) * 20
        y_comida = round(random.randrange(0, 600 - z) / 20) * 20

    pygame.draw.rect(tela, cinza, [x_comida, y_comida, z, z])

    return x_comida, y_comida, posicao

def parede(posicao):
    cabeca = posicao[-1]
    x = cabeca[0]
    y = cabeca[1]

    if x not in range(600) or y not in range(600):
        raise Exception

def bateu(posicao):
    cabeca = posicao[-1]
    corpo = posicao.copy()

    del corpo[-1]

    for x, y in corpo:
        if x == cabeca[0] and y == cabeca[1]:
            raise Exception

def score(posicao):
    calculo = str(len(posicao))
    pontos = fonte.render('Score: ' + calculo, True, cinza)
    tela.blit(pontos, [20, 20])

# Definir tempo
tempo = pygame.time.Clock()

# Loop até perder
while True:
    pygame.display.update()

    snake(posicao)
    dx, dy, posicao = mover(dx, dy, posicao)
    x_comida, y_comida, posicao = comida(dx, dy, x_comida, y_comida, posicao)
    parede(posicao)
    bateu(posicao)
    score(posicao)
    
    tempo.tick(10)

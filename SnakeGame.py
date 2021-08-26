# Importar biblioteca do PyGame para fazer o jogo
import pygame
import random

# Iniciar todos os módulos do PyGame
pygame.init()

# Cores em RGB
black = (38, 38, 38)
red = (245, 0, 37)
blue = (155, 177, 255)
gray = (163, 165, 195)

# Dimensões da tela = 600 x 600
dimensoes = (600, 600)

# Posição inicial da cobrinha no centro da tela
x = 300
y = 300

# Corpo da cobrinha
z = 10

# Agrupar x e y em lista para chamar os dois de uma vez
listaSnake = [[x, y]]

# Para a cobra poder se movimentar na vertical e horizontal
delta_x = 0
delta_y = 0

# Comida que aumenta o tamanho da cobrinha
comida_x = round(random.randrange(0, 600 - z) / 10) * 10
comida_y = round(random.randrange(0, 600 - z) / 10) * 10

# Fonte
fonte = pygame.font.SysFont('hack', 30)

# Pegar assets (templates) do PyGame
tela = pygame.display.set_mode(dimensoes) # set_mode = exibe uma tela com as dimensões atribuidas
pygame.display.set_caption('Snake Game') # set_caption = define o título na tela
     # display = criar janela

# Preencher (.fill) a tela com a cor atribuida
tela.fill(black)

# Relógio com o tempo de jogo
tempo = pygame.time.Clock()

def drawSnake(listaSnake):
    tela.fill(black)

    for i in listaSnake:
        pygame.draw.rect(tela, red, [i[0], i[1], z, z]) # rect = criar áreas retangulares
                                              # 10 x 10 -> corpo inicial da cobrinha

def moveSnake(delta_x, delta_y, listaSnake):
    # Alterar posição da cobrinha de acordo com as setas clicadas
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_x = -z # z = corpo da cobrinha
                delta_y = 0
            elif event.key == pygame.K_RIGHT:
                delta_x = z
                delta_y = 0
            elif event.key == pygame.K_UP:
                delta_x = 0
                delta_y = -z
            elif event.key == pygame.K_DOWN:
                delta_x = 0
                delta_y = z

    # Percorre desde: [Último item][Primeiro item]
    new_x = listaSnake[-1][0] + delta_x
    new_y = listaSnake[-1][1] + delta_y
    listaSnake.append([new_x, new_y]) # append = adiciona um item no fim da lista

    # Deletar primeiro item da lista
    del listaSnake[0] # para que a cobrinha ande sem aumentar de tamanho

    return delta_x, delta_y, listaSnake

# Aumentar a cobra de tamanho se ela comer
def comida(delta_x, delta_y, comida_x, comida_y, listaSnake,):
    head = listaSnake[-1]

    x_novo = head[0] + delta_x
    y_novo = head[1] + delta_y

    if head[0] == comida_x and head[1] == comida_y:
        listaSnake.append([x_novo, y_novo])
        # Para fazer a comida aparecer em outro local aleatório da tela
        comida_x = round(random.randrange(0, 600 - z) / 10) * 10
        comida_y = round(random.randrange(0, 600 - z) / 10) * 10

    # Pygame desenhe retângulo
    pygame.draw.rect(tela, blue, [comida_x, comida_y, z, z])

    return comida_x, comida_y, listaSnake

# Se a cobra tocar na parede, Game Over
def parede(listaSnake):
    head = listaSnake[-1]
    x = head[0]
    y = head[1]

    # Dimensões da tela: range(600) = [0, ..., 599]
    if x not in range(600) or y not in range(600):
        raise Exception # quebra o loop e fecha jogo

# Se a cobra se tocar, Game Over
def seTocou(listaSnake):
    head = listaSnake[-1]
    body = listaSnake.copy()

    del body[-1]

    for x, y in body:
        if x == head[0] and y == head[1]:
            raise Exception

# Pontuação na tela
def pontos(listaSnake):
    points = str(len(listaSnake))
    score = fonte.render('Score: ' + points, True, gray)
    tela.blit(score, [20, 20]) # Posição do score na tela

# Loop até vencer
while True:
    pygame.display.update() # update = atualiza a tela

    drawSnake(listaSnake)
    # 1 clique na seta = direção (cobrinha corre sem parar)
    delta_x, delta_y, listaSnake = moveSnake(delta_x, delta_y, listaSnake)
    comida_x, comida_y, listaSnake = comida(delta_x, delta_y, comida_x, comida_y, listaSnake)
    parede(listaSnake)
    seTocou(listaSnake)
    pontos(listaSnake)

    tempo.tick(10) # tempo para a cobrinha se mover após o clique (quanto maior, mais rápido)
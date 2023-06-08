import random
from os import system


# variaveis globais
pos_pacman = [0, 0]
matriz = [['.' for coluna in range(15)] for linha in range(10)]
score = 0


# printar as linhas sem [] , ''
def formatar_linha(linha):
    nova_linha = ' '.join(linha)
    return nova_linha


# gerar frutas
def gerar_fruta(matriz):
    pos_linha = random.randint(0, len(matriz) -1)
    pos_coluna = random.randint(0, len(matriz[0]) -1)

    return [pos_linha, pos_coluna]

# texto verde e amarelo
def txt_verde(texto):
    return f'\033[32m{texto}\033[0m'

def txt_amarelo(texto):
    return f'\033[33m{texto}\033[0m'


# itera a matriz e mostra o mapa na tela
def mostrar_mapa(matriz=matriz):
    system('cls')

    print(txt_verde('[PACMAN]'), ' '*9, txt_amarelo(f'[SCORE]: {score}'))
    [print(formatar_linha(linha)) for linha in matriz]


# tira o pacman e coloca em outro canto
def mostrar_pacman(tamanho):
    # procura o pacman e coloca um ponto no lugar
    for linha_index, linha in enumerate(matriz):
        for coluna_index, coluna in enumerate(linha):
            if coluna in ['o', 'O']:
                matriz[linha_index][coluna_index] = '.'

    matriz[pos_pacman[0]][pos_pacman[1]] = tamanho
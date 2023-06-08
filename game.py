from keyboard import is_pressed
from winsound import Beep
from time import sleep

import utils

if __name__ == '__main__':
    iterador_movimento = 0

    pos_fruta = utils.gerar_fruta(utils.matriz)
    utils.matriz[pos_fruta[0]][pos_fruta[1]] = '♫'

    while not is_pressed('Esc'):
        if utils.score > 9:
            utils.mostrar_mapa()
            break

        utils.mostrar_pacman('o') if (iterador_movimento % 2 == 0) else utils.mostrar_pacman('O')
        iterador_movimento += 1

        utils.mostrar_mapa()
        sleep(0.2)

        # mover o pacman
        if utils.pos_pacman != pos_fruta:
            # linhas
            if utils.pos_pacman[0] != pos_fruta[0]:
                if utils.pos_pacman[0] < pos_fruta[0]:
                    utils.pos_pacman[0] += 1
                
                else:
                    utils.pos_pacman[0] -= 1

            # colunas
            elif utils.pos_pacman[1] != pos_fruta[1]:
                if utils.pos_pacman[1] < pos_fruta[1]:
                    utils.pos_pacman[1] += 1
                
                else:
                    utils.pos_pacman[1] -= 1

        else:
            Beep(1500, 10)
            Beep(2000, 10)
            utils.score += 1

            pos_fruta = utils.gerar_fruta(utils.matriz)
            utils.matriz[pos_fruta[0]][pos_fruta[1]] = '♫'
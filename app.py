import keyboard
import winsound
import time
import os

from pacman import display_map, display_pac, pacman_pos, matrix
import utils

if __name__ == '__main__':
    pac_iterator = 0

    while keyboard.is_pressed('Esc') == False:
        display_pac('o') if (pac_iterator % 2 == 0) else display_pac('O')
        pac_iterator += 1

        # insert fruit if doesn't exist one
        if not any('♫' in line for line in matrix):
            next_fruit = utils.generate_fruit(matrix)
            matrix[next_fruit[0]][next_fruit[1]] = '♫'

        os.system('cls')
        display_map()
        time.sleep(0.2)

        # move pacman
        if pacman_pos != next_fruit:
                # lines
                if pacman_pos[0] != next_fruit[0]:
                    if pacman_pos[0] < next_fruit[0]:
                        pacman_pos[0] += 1

                    else:
                        pacman_pos[0] -= 1

                # columns
                if pacman_pos[1] != next_fruit[1]:
                    if pacman_pos[1] < next_fruit[1]:
                        pacman_pos[1] += 1

                    else:
                        pacman_pos[1] -= 1

        else:
            winsound.Beep(1500, 10)
            winsound.Beep(2000, 10)

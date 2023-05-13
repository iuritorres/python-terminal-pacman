import time
import os

from pacman import display_map, display_pac, pacman_pos, fruits_pos
import utils

if __name__ == '__main__':
    pac_iterator = 0

    while len(fruits_pos) != 0:
        display_pac('o') if (pac_iterator % 2 == 0) else display_pac('O')
        pac_iterator += 1

        os.system('cls')
        display_map()
        time.sleep(0.2)

        # up and down
        next_fruit = utils.closest_fruit(fruits_pos)

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
            fruits_pos.remove(next_fruit)

import os
import pacman

if __name__ == '__main__':
    os.system('cls')

    matrix = [['.' for space in range(20)] for line in range(15)]

    pacman.display_pac(matrix)

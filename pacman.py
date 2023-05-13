import keyboard

import utils


# pos[1] left/right ---- pos[0] up/down
fruits_pos = []
pacman_pos = [0, 0]

matrix = [['.' for space in range(15)] for line in range(10)]


# display the map in terminal, with a 10x15 default matrix
def display_map(matrix: list = matrix) -> None:
    [print(utils.format_line(line)) for line in matrix]


# pacman position logics
def display_pac(size: str, new_pos: list = pacman_pos) -> None:
    # find pacman last pos and replace '.'
    for lineIndex, line in enumerate(matrix):
        for columnIndex, column in enumerate(line):
            if column == 'o' or column == 'O':
                matrix[lineIndex][columnIndex] = '.'

    # (lines) if pos > map_size, go to start
    if new_pos[0] < 0:
        pacman_pos[0] = len(matrix) - 1

    elif new_pos[0] > len(matrix) - 1:
        pacman_pos[0] = 0

    # (column) if pos > map_size, go to start
    elif new_pos[1] < 0:
        pacman_pos[1] = len(matrix[0]) - 1

    elif new_pos[1] > len(matrix[0]) - 1:
        pacman_pos[1] = 0

    else:
        matrix[new_pos[0]][new_pos[1]] = size


# insert fruits in matrix
for i in range(11):
    pos = utils.generate_fruit(matrix)
    fruits_pos.append(pos)

    matrix[pos[0]][pos[1]] = 'X'

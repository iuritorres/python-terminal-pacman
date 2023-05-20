import utils

# pos[0] up/down
# pos[1] left/right
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
            if column in ['o', 'O']:
                matrix[lineIndex][columnIndex] = '.'    

    else:
        matrix[new_pos[0]][new_pos[1]] = size

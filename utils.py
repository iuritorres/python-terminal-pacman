import math
import random

# delete unnecessary chars in list
def format_line(list: list) -> str:
    remove_chars = ['[', ']', "'", ',']
    new_list = str(list)

    for char in remove_chars:
        new_list = new_list.replace(char, '')

    return new_list

# generate fruits
def generate_fruit(matrix: list) -> list:
    lineIndex = random.randint(0, len(matrix) -1)
    columnIndex = random.randint(0, len(matrix[0]) -1)

    return [lineIndex, columnIndex]

# search the closest fruit
def closest_fruit(fruits_pos: list) -> list:
    next_pos = []

    # closest_axis = min(next_fruit)
    # axis = next_fruit.index(closest_axis)

    # get closest line
    for pos in fruits_pos:
        next_pos.append(pos[0])

    closest_line = min(next_pos)

    # reset next_pos list
    next_pos.clear()

    # get closest column
    for pos in fruits_pos:
        if pos[0] == closest_line:
            next_pos.append(pos[1])

    closest_column = min(next_pos)

    return [closest_line, closest_column]

# pos = [[4, 11], [6, 13], [1, 6]]
# print(closest_fruit(pos))
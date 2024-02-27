"""GameMap class' module"""


from random import randint
from pacman import Pacman
from utils import Utils, TerminalColors


class GameMap:
    """GameMap class"""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.matrix = [['.' for column in range(self.width)]
                       for line in range(self.height)]

        self.pacman = Pacman()
        self.fruit_position = {"x": 0, "y": 0}

    @staticmethod
    def _format_line(line: str) -> str:
        """Return a line without special characters ([] , '') """

        return " ".join(line)

    def show(self) -> None:
        """Displays the game map in terminal"""

        for line in self.matrix:
            print(self._format_line(line))

    def generate_fruit(self) -> None:
        """Generate fruit and insert it into self.matrix"""

        index_line = randint(0, len(self.matrix) - 1)
        index_column = randint(0, len(self.matrix[0]) - 1)

        self.matrix[index_line][index_column] = Utils.colored_text('♫',
                                                                   TerminalColors.MAGENTA)
        self.fruit_position = {
            "x": index_column,
            "y": index_line
        }

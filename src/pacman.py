"""Pacman class' module"""


class Pacman:
    """Pacman class"""

    _INITIAL_STATE = "o"

    def __init__(self) -> None:
        self.matrix = [[]]
        self.current_state = self._INITIAL_STATE
        self.position = {"x": 0, "y": 0}

    def move(self):
        """Move pacman to other cell"""

        for line_index, line in enumerate(self.matrix):
            for column_index, column in enumerate(line):
                if column in ["o", "O"]:
                    self.matrix[line_index][column_index] = "."

        if self.current_state == self._INITIAL_STATE:
            self.current_state = "O"
        else:
            self.current_state = self._INITIAL_STATE

        self.matrix[self.position["y"]
                    ][self.position["x"]] = self.current_state

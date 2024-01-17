"""Main game module"""


from os import system
from winsound import PlaySound, SND_FILENAME, SND_ASYNC
from time import sleep
from pacman import Pacman
from game_map import GameMap
from utils import Utils, TerminalColors


class Game:
    """Main game class"""

    _REQUIRED_SCORE = 5

    def __init__(self, pacman: Pacman, maps: list[GameMap]) -> None:
        self.pacman = pacman
        self.maps = maps
        self.current_map = self.maps[0]
        self.score = 0

        self._build_game()

    def _build_game(self) -> None:
        """Configure pacman"s matrix and set him in current game map"""

        self.pacman.matrix = self.current_map.matrix

        for game_map in self.maps:
            game_map.pacman = self.pacman

    def _end(self, victory: bool) -> None:
        """Finish game"""

        self._show_score_map()

        if victory:
            PlaySound("src\\sounds\\victory.wav", SND_FILENAME)
        else:
            PlaySound("src\\sounds\\pacman_death.wav", SND_FILENAME)

    def _show_score(self) -> None:
        """Print game score in terminal"""

        print(Utils.colored_text("[PACMAN]", TerminalColors.YELLOW), end="")
        print(" "*10, end="")
        print(Utils.colored_text(f"[SCORE]: {self.score}",
                                 TerminalColors.GREEN))

    def _main_loop(self):
        """Main game loop"""

        while True:
            if self._did_win():
                self._end(victory=True)
                break

            self._show_score_map()
            sleep(0.2)

            # Moves pacman
            if self.pacman.position != self.current_map.fruit_position:
                # Lines
                if self.pacman.position["y"] != self.current_map.fruit_position["y"]:
                    if self.pacman.position["y"] < self.current_map.fruit_position["y"]:
                        self.pacman.position["y"] += 1

                    else:
                        self.pacman.position["y"] -= 1

                # Columns
                elif self.pacman.position["x"] != self.current_map.fruit_position["x"]:
                    if self.pacman.position["x"] < self.current_map.fruit_position["x"]:
                        self.pacman.position["x"] += 1

                    else:
                        self.pacman.position["x"] -= 1

                self.pacman.move()

            else:
                PlaySound("src\\sounds\\pacman_eatfruit.wav",
                          SND_FILENAME | SND_ASYNC)

                self.score += 1

                if not self._did_win():
                    self.current_map.generate_fruit()

    def _show_score_map(self) -> None:
        """Shows score and map in terminal"""

        system("cls")
        self._show_score()
        self.current_map.show()

    def _did_win(self) -> bool:
        """Returns if the required score has been reached"""

        return self.score >= self._REQUIRED_SCORE

    def start(self) -> None:
        """Starts game"""

        # LETRERO MASSA DO PACMAN ( TENTAR NE )

        self.current_map.generate_fruit()
        self.pacman.move()
        self._show_score_map()

        PlaySound("src\\sounds\\pacman_beginning.wav", SND_FILENAME)

        self._main_loop()


if __name__ == "__main__":
    game = Game(
        pacman=Pacman(),
        maps=[GameMap(
            width=15,
            height=10
        )]
    )

    game.start()

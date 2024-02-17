"""Provides a score manager class"""
from utils import Utils, TerminalColors

# pylint: disable=too-few-public-methods
class Score:
    """Score manager class"""

    def __init__(self, points: int = 0) -> None:
        self.points = points

    def show(self) -> None:
        """Print game score in terminal"""

        print(Utils.colored_text("[PACMAN]", TerminalColors.YELLOW), end="")
        print(" "*10, end="")
        print(Utils.colored_text(f"[SCORE]: {self.points:>2}",
                                 TerminalColors.GREEN))

"""Provides utilities classes"""


from enum import StrEnum


class TerminalColors(StrEnum):
    """A Set of python suported terminal colors"""

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"


class Utils:
    """Provides utilities methods"""

    @staticmethod
    def colored_text(text: str, color: TerminalColors) -> str:
        """Returns a colored text based on color parameter"""

        return f"{color}{text}{TerminalColors.RESET}"

"""
Provides the Responsible class to make the
Pacman's sign at the beginning of the game
"""

import os
from time import sleep
from winsound import PlaySound, SND_FILENAME, SND_ASYNC
from dataclasses import dataclass


# pylint: disable=too-few-public-methods
class SignDisplayer:
    """Utility class to display signs."""

    @staticmethod
    def display(sign: str, sound: str, duration: float) -> None:
        """Display a sign in the terminal from left to right."""

        PlaySound(sound, SND_FILENAME | SND_ASYNC)

        line_size = len(sign[0])

        for index in range(line_size - 1):
            os.system('cls')

            column = [line[:index + 1] for line in sign]

            print(str("\n".join(column)))
            sleep(duration)


@dataclass
class AvailableSigns:
    """A Set of python suported terminal colors"""

    # pylint: disable=line-too-long
    # Font: georgia11
    PACMAN = ['`7MM"""Mq.' + "       db        .g8" + '""bgd  `7MMM.     ,MMF' + "'      db      `7MN.   `7MF'",
              "  MM   `MM.     ;MM:     .dP'     `M   MMMb    dPMM       ;MM:       MMN.    M  ",
              "  MM   ,M9     ,V^MM.    dM'       `   M YM   ,M MM      ,V^MM.      M YMb   M  ",
              "  MMmmdM9     ,M  `MM    MM            M  Mb  M' MM     ,M  `MM      M  `MN. M  ",
              "  MM          AbmmmqMA   MM.           M  YM.P'  MM     AbmmmqMA     M   `MM.M  ",
              "  MM         A'     VML  `Mb.     ,'   M  `YM'   MM    A'     VML    M     YMM  ",
              ".JMML.     .AMA.   .AMMA.  `" + '"bmmmd' + "'  .JML. `'  .JMML..AMA.   .AMMA..JML.    YM  "]

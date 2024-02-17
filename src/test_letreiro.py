import sys
import os
from time import sleep
from winsound import PlaySound, SND_FILENAME, SND_ASYNC

# Font: georgia11
# pylint: disable=line-too-long
lines = ['`7MM"""Mq.' + "       db        .g8" + '""bgd  `7MMM.     ,MMF' + "'      db      `7MN.   `7MF'",
         "  MM   `MM.     ;MM:     .dP'     `M   MMMb    dPMM       ;MM:       MMN.    M  ",
         "  MM   ,M9     ,V^MM.    dM'       `   M YM   ,M MM      ,V^MM.      M YMb   M  ",
         "  MMmmdM9     ,M  `MM    MM            M  Mb  M' MM     ,M  `MM      M  `MN. M  ",
         "  MM          AbmmmqMA   MM.           M  YM.P'  MM     AbmmmqMA     M   `MM.M  ",
         "  MM         A'     VML  `Mb.     ,'   M  `YM'   MM    A'     VML    M     YMM  ",
         ".JMML.     .AMA.   .AMMA.  `" + '"bmmmd' + "'  .JML. `'  .JMML..AMA.   .AMMA..JML.    YM  "]

PlaySound("src\\sounds\\pacman_beginning.wav",
          SND_FILENAME | SND_ASYNC)

for index in range(len(lines[0]) - 1):
    os.system('cls')

    column = [line[:index + 1] for line in lines]

    print(str("\n".join(column)))

    sleep(0.027)

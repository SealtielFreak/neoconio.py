import random
import time

from neoconio import *

ship = (
    " ^ ",
    "/|\\"
)


def main():
    x, y = 0, 0

    while True:
        textbackground('black')
        cputsxy(0, 0, "Hello world")

        italichigh()
        textbackground('red')
        cputsxy(0, 1, "Hello world")
        italiclow()

        k = kbhit()

        if k == "w":
            y -= 1
        elif k == "s":
            y += 1

        if k == "a":
            x -= 1
        elif k == "d":
            x += 1

        highvideo()
        cputsxy(x, y, ship[0])
        cputsxy(x, y + 1, ship[1])
        lowvideo()

        delay(30)
        clrscr()


if __name__ == '__main__':
    set_main_loop_thread(target=main)

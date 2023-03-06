import typing

from neoconio.backend import Console

__console = Console(80, 30)


def getbuffersize() -> typing.Tuple[int, int]:
    return __console.getbuffersize()


def wasinit() -> int:
    pass


def initconio(flags: int) -> int:
    pass


def quitconio() -> None:
    pass


def scalewindow(scale: int) -> None:
    __console.scalewindow(scale)


def titlewindow(title: str) -> None:
    __console.titlewindow(title)


def loadfont(filename: str) -> int:
    __console.set_filename_font(filename)


def resize(columns: int, rows: int) -> None:
    __console.resize(columns, rows)


def refresh() -> int:
    return __console.refresh()


def gettextinfo():
    pass


def inittextinfo() -> None:
    pass


def clreol() -> None:
    __console.clreol()


def clrscr() -> None:
    __console.clrscr()


def delline() -> None:
    __console.delline()


def insline() -> None:
    __console.insline()


def _conio_gettext(left: int, top: int, right: int, bottom: int, char_info) -> None: ...


def puttext(left: int, top: int, right: int, bottom: int) -> None: ...


def movetext(left: int, top: int, right: int, bottom: int, destleft: int, desttop: int) -> None: ...


def gotoxy(x: int, y: int) -> None:
    __console.gotoxy(x, y)


def cputsxy(x: int, y: int, _str: str) -> None:
    __console.cputsxy(x, y, _str)


def putchxy(x: int, y: int, _chr: chr) -> None:
    __console.putchxy(x, y, _chr)


def _setcursortype(type: int) -> None:
    pass


def textattr(attr: int) -> None:
    __console.textattr(attr)


def normvideo() -> None:
    __console.normvideo()


def textbackground(color: int) -> None:
    __console.textbackground(color)


def textcolor(color: int) -> None:
    __console.textcolor(color)


def wherex() -> int:
    return __console.wherex()


def wherey() -> int:
    return __console.wherey()


def getpass(prompt: str, _str: str) -> str:
    return __console.getpass(prompt, _str)


def highvideo() -> None:
    __console.highvideo()


def lowvideo() -> None:
    __console.lowvideo()


def delay(ms: int) -> None:
    __console.delay(ms)


def switchbackground(color: int) -> None:
    __console.switchbackground(color)


def flashbackground(color: int, ms: int) -> None:
    __console.flashbackground(color, ms)


def clearkeybuf() -> None:
    __console.clearkeybuf()


def kbhit() -> int:
    return __console.kbhit()


def getch() -> int:
    return __console.getch()


def getche() -> int:
    return __console.getche()

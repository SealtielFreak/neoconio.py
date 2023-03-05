import typing


from neoconio.backend import Console


__console = Console(80, 30)


def getbuffersize() -> typing.Tuple[int, int]:
    pass


def wasinit() -> int:
    pass


def initconio(flags: int) -> int:
    pass


def quitconio() -> None:
    pass


def scalewindow(scale: int) -> None:
    pass


def titlewindow(title: str) -> None:
    pass


def loadfont(filename: str) -> int:
    pass


def resize(columns: int, rows: int) -> None:
    pass


def refresh() -> int:
    pass


def gettextinfo():
    pass


def inittextinfo() -> None:
    pass


def clreol() -> None:
    pass


def clrscr() -> None:
    pass


def delline() -> None:
    pass


def insline() -> None:
    pass


def _conio_gettext(left: int, top: int, right: int, bottom: int, char_info) -> None:
    pass


def puttext(left: int, top: int, right: int, bottom: int, char_info) -> None:
    pass


def movetext(left: int, top: int, right: int, bottom: int, destleft: int, desttop: int) -> None:
    pass


def gotoxy(x: int, y: int) -> None:
    pass


def cputsxy(x: int, y: int, _str: str) -> None:
    pass


def putchxy(x: int, y: int, ch: chr) -> None:
    pass


def _setcursortype(type: int) -> None:
    pass


def textattr(attr: int) -> None:
    pass


def normvideo() -> None:
    pass


def textbackground(color: int) -> None:
    pass


def textcolor(color: int) -> None:
    pass


def wherex() -> int:
    pass


def wherey() -> int:
    pass


def getpass(prompt: str, str: str) -> str:
    pass


def highvideo() -> None:
    pass


def lowvideo() -> None:
    pass


def delay(ms: int) -> None:
    pass


def switchbackground(color: int) -> None:
    pass


def flashbackground(color: int, ms: int) -> None:
    pass


def clearkeybuf() -> None:
    pass


def kbhit() -> int:
    pass


def getch() -> int:
    pass


def getche() -> int:
    pass

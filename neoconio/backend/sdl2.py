import typing

import neoconio.abc.console


class SDL2Console(neoconio.abc.console.Console):
    def set_runtime(self, runtime: neoconio.abc.runtime.RuntimeLoop):
        pass

    @property
    def runtime(self):
        pass

    def main_loop(self, target):
        pass

    def set_filename_font(self, filename: str):
        pass

    @property
    def filename_font(self):
        pass

    def getbuffersize(self) -> typing.Tuple[int, int]:
        pass

    @property
    def buffersize(self):
        pass

    def scalewindow(self, scale: int) -> None:
        pass

    def titlewindow(self, title: typing.Text) -> None:
        pass

    @property
    def title(self):
        pass

    def resize(self, columns: int, rows: int) -> None:
        pass

    def refresh(self) -> int:
        pass

    def gettextinfo(self) -> neoconio.abc.dataclass.TextInfo:
        pass

    def inittextinfo(self) -> None:
        pass

    def clreol(self) -> None:
        pass

    def clrscr(self) -> None:
        pass

    def delline(self) -> None:
        pass

    def insline(self) -> None:
        pass

    def conio_gettext(self, left: int, top: int, right: int, bottom: int, char_info) -> None:
        pass

    def puttext(self, left: int, top: int, right: int, bottom: int, char_info) -> None:
        pass

    def movetext(self, left: int, top: int, right: int, bottom: int, destleft: int, desttop: int) -> None:
        pass

    def gotoxy(self, x: int, y: int) -> None:
        pass

    def print(self, _str: str):
        pass

    def cputsxy(self, x: int, y: int, _str: str) -> None:
        pass

    def putchxy(self, x: int, y: int, ch: chr) -> None:
        pass

    def _setcursortype(self, type: int) -> None:
        pass

    def textattr(self, attr: int) -> None:
        pass

    def normvideo(self) -> None:
        pass

    def textbackground(self, color: int) -> None:
        pass

    def textcolor(self, color: int) -> None:
        pass

    def wherex(self) -> int:
        pass

    def wherey(self) -> int:
        pass

    def getpass(self, prompt: str, str: str) -> str:
        pass

    def highvideo(self) -> None:
        pass

    def lowvideo(self) -> None:
        pass

    def delay(self, ms: int) -> None:
        pass

    def switchbackground(self, color: int) -> None:
        pass

    def flashbackground(self, color: int, ms: int) -> None:
        pass

    def clearkeybuf(self) -> None:
        pass

    def kbhit(self) -> int:
        pass

    def getch(self) -> int:
        pass

    def getche(self) -> int:
        pass

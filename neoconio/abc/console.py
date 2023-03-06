import abc
import typing

import neoconio.abc.dataclass
import neoconio.abc.runtime
import neoconio.colors


class Console:
    U_CHR_MAX = 255 * 2
    DEFAULT_TITLE = ""
    DEFAULT_SIZE = 640, 480

    @property
    @abc.abstractmethod
    def resizable(self) -> bool: ...

    @resizable.setter
    @abc.abstractmethod
    def resizable(self, _resizable: bool): ...

    @abc.abstractmethod
    def set_runtime(self, runtime: neoconio.abc.runtime.RuntimeLoop): ...

    @property
    @abc.abstractmethod
    def runtime(self): ...

    @abc.abstractmethod
    def main_loop(self, target): ...

    @abc.abstractmethod
    def set_filename_font(self, filename: str): ...

    @property
    @abc.abstractmethod
    def filename_font(self): ...

    @abc.abstractmethod
    def getbuffersize(self) -> typing.Tuple[int, int]: ...

    @property
    @abc.abstractmethod
    def buffersize(self): ...

    @abc.abstractmethod
    def scalewindow(self, scale: int) -> None: ...

    @abc.abstractmethod
    def titlewindow(self, title: typing.Text) -> None: ...

    @property
    @abc.abstractmethod
    def title(self): ...

    @abc.abstractmethod
    def resize(self, columns: int, rows: int) -> None: ...

    @abc.abstractmethod
    def refresh(self) -> int: ...

    @abc.abstractmethod
    def gettextinfo(self) -> neoconio.abc.dataclass.TextInfo: ...

    @abc.abstractmethod
    def inittextinfo(self) -> None: ...

    @abc.abstractmethod
    def clreol(self) -> None: ...

    @abc.abstractmethod
    def clrscr(self) -> None: ...

    @abc.abstractmethod
    def delline(self) -> None: ...

    @abc.abstractmethod
    def insline(self) -> None: ...

    @abc.abstractmethod
    def conio_gettext(self, left: int, top: int, right: int, bottom: int, char_info) -> None: ...

    @abc.abstractmethod
    def puttext(self, left: int, top: int, right: int, bottom: int, char_info) -> None: ...

    @abc.abstractmethod
    def movetext(self, left: int, top: int, right: int, bottom: int, destleft: int, desttop: int) -> None: ...

    @abc.abstractmethod
    def gotoxy(self, x: int, y: int) -> None: ...

    @abc.abstractmethod
    def printf(self, _str: str, *args, **kwargs): ...

    @abc.abstractmethod
    def cputsxy(self, x: int, y: int, _str: str) -> None: ...

    @abc.abstractmethod
    def putchxy(self, x: int, y: int, ch: chr) -> None: ...

    @abc.abstractmethod
    def _setcursortype(self, type: int) -> None: ...

    @abc.abstractmethod
    def textattr(self, attr: int) -> None: ...

    @abc.abstractmethod
    def normvideo(self) -> None: ...

    @abc.abstractmethod
    def textbackground(self, color: neoconio.colors.Color) -> None: ...

    @abc.abstractmethod
    def textcolor(self, color: neoconio.colors.Color) -> None: ...

    @abc.abstractmethod
    def wherex(self) -> int: ...

    @abc.abstractmethod
    def wherey(self) -> int: ...

    @abc.abstractmethod
    def getpass(self, prompt: str, _str: str) -> str: ...

    @abc.abstractmethod
    def highvideo(self) -> None: ...

    @abc.abstractmethod
    def lowvideo(self) -> None: ...

    @abc.abstractmethod
    def delay(self, ms: int) -> None: ...

    @abc.abstractmethod
    def switchbackground(self, color: int) -> None: ...

    @abc.abstractmethod
    def flashbackground(self, color: int, ms: int) -> None: ...

    @abc.abstractmethod
    def clearkeybuf(self) -> None: ...

    @abc.abstractmethod
    def kbhit(self) -> int: ...

    @abc.abstractmethod
    def getch(self) -> int: ...

    @abc.abstractmethod
    def getche(self) -> int: ...

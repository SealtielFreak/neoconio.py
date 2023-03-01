import abc
import dataclasses
import typing

from neoconio.colors import Color


@dataclasses.dataclass
class TextInfo:
    curx: int
    cury: int
    attribute: int
    normattribute: int
    screenwidth: int
    screenheight: int


@dataclasses.dataclass
class CharInfo:
    letter: chr
    attr: int


create_matrix = lambda cols, rows, value: [[value for _ in range(cols)] for _ in range(rows)]


class Console:
    U_CHR_MAX = 255
    DEFAULT_TITLE = ""
    DEFAULT_SIZE = 640, 480

    def __init__(self, cols: int = 80, rows: int = 30):
        self.__current_cursor = 0, 0
        self.__title = Console.DEFAULT_TITLE
        self.__font_filename = ''
        self.__matrix_shape = cols, rows
        self.__matrix_chr = create_matrix(cols, rows, ' ')
        self.__matrix_colors_foreign = create_matrix(cols, rows, Color.WHITE)
        self.__matrix_colors_background = create_matrix(cols, rows, Color.BLACK)

    @abc.abstractmethod
    def main_loop(self, f_main_loop): ...

    def set_filename_font(self, filename: str):
        self.__font_filename = filename

    @property
    def filename_font(self):
        return self.__font_filename

    def getbuffersize(self) -> typing.Tuple[int, int]:
        return self.__matrix_shape

    @property
    def buffersize(self):
        return self.getbuffersize()

    def scalewindow(self, scale: int) -> None:
        pass

    def titlewindow(self, title: typing.Text) -> None:
        self.__title = title

    @property
    def title(self):
        return self.__title

    def resize(self, columns: int, rows: int) -> None:
        self.__current_cursor = columns, rows

    def refresh(self) -> int:
        pass

    def gettextinfo(self) -> TextInfo:
        pass

    def inittextinfo(self) -> None:
        pass

    def clreol(self) -> None:
        pass

    def clrscr(self) -> None:
        self.__matrix_chr = create_matrix(*self.buffersize, ' ')

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
        self.__current_cursor = [x, y]

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
        return self.__current_cursor[0]

    def wherey(self) -> int:
        return self.__current_cursor[1]

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

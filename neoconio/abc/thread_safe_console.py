import abc
import time
import typing

import neoconio.abc.console
import neoconio.abc.dataclass
import neoconio.abc.runtime
import neoconio.colors

zero_array2d = lambda cols, rows, value: [[value for _ in range(cols)] for _ in range(rows)]


def memset_array2d(a, b):
    for y, row in enumerate(a):
        for x, c in enumerate(a):
            try:
                b[y][x] = a[y][x]
            except IndexError:
                pass

    return b


def check_array2d(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False

    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                return False

    return True


class ThreadSafeConsole(neoconio.abc.console.Console):
    U_CHR_MAX = 255
    DEFAULT_TITLE = ""
    DEFAULT_SIZE = 640, 480

    def __init__(self, cols: int = 80, rows: int = 30):
        self.__resizable = True
        self.__runtime = None
        self.__current_cursor = 0, 0
        self.__title = ThreadSafeConsole.DEFAULT_TITLE
        self.__font_filename = ''
        self.__shape = cols, rows
        self.__matrix = zero_array2d(cols, rows, ' ')
        self.__matrix_colors_fg = zero_array2d(cols, rows, neoconio.colors.Color.WHITE)
        self.__matrix_colors_bk = zero_array2d(cols, rows, neoconio.colors.Color.BLACK)

    @property
    def resizable(self) -> bool:
        return self.__resizable

    @resizable.setter
    def resizable(self, _resizable: bool):
        self.__resizable = _resizable

    @property
    def cursor(self):
        return tuple(self.__current_cursor)

    @property
    def shape(self) -> typing.Tuple[int, int]:
        return self.__shape

    @property
    def matrix(self) -> typing.List[typing.List[chr]]:
        return self.__matrix

    def set_runtime(self, runtime: neoconio.abc.runtime.RuntimeLoop):
        self.__runtime = runtime

    @property
    def runtime(self):
        return self.__runtime

    def set_filename_font(self, filename: str):
        self.__font_filename = filename

    @property
    def filename_font(self):
        return self.__font_filename

    def getbuffersize(self) -> typing.Tuple[int, int]:
        return self.__shape

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
        self.__shape = columns, rows
        self.__matrix = memset_array2d(self.matrix, zero_array2d(columns, rows, ' '))

    def refresh(self) -> int:
        pass

    def gettextinfo(self) -> neoconio.abc.dataclass.TextInfo:
        pass

    def inittextinfo(self) -> None:
        pass

    def clreol(self) -> None:
        pass

    def clrscr(self) -> None:
        self.__matrix = zero_array2d(*self.buffersize, ' ')

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
        self.__current_cursor = [x % self.shape[0], y % self.shape[1]]

    def printf(self, _str: str, *args, **kwargs):
        self.cputsxy(self.wherex(), self.wherey(), _str)

    def cputsxy(self, x: int, y: int, _str: str) -> None:
        for _chr in _str:
            x += 1

            if _chr == '\n':
                _chr = ''
                y += 1
                x = 0

            self.putchxy(x, y, _chr)

    def putchxy(self, x: int, y: int, _chr: chr) -> None:
        self.gotoxy(x, y)

        try:
            self.matrix[self.wherey()][self.wherex()] = _chr
        except IndexError:
            pass

    def _setcursortype(self, type: int) -> None:
        pass

    def textattr(self, attr: int) -> None:
        pass

    def normvideo(self) -> None:
        pass

    def textbackground(self, color: neoconio.colors.Color) -> None:
        pass

    def textcolor(self, color: neoconio.colors.Color) -> None:
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
        time.sleep(ms / 1000)

    def switchbackground(self, color: neoconio.colors.Color) -> None:
        pass

    def flashbackground(self, color: int, ms: int) -> None:
        pass

    def clearkeybuf(self) -> None:
        pass

    @abc.abstractmethod
    def kbhit(self) -> chr: ...

    @abc.abstractmethod
    def getch(self) -> chr: ...

    @abc.abstractmethod
    def getche(self) -> chr: ...

    @abc.abstractmethod
    def main_loop(self, target: typing.Callable[[None], None]): ...

import collections
import dataclasses
import threading
import typing

import pygame

DEFAULT_SIZE = 80, 30

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


@dataclasses.dataclass
class Cursor:
    x: int = 0
    y: int = 0

    def __iter__(self):
        return iter((self.x, self.y))


@dataclasses.dataclass
class BufferCharacter:
    char: chr = ''
    background: str = 'black'
    foreign: str = 'black'
    bold: bool = False
    italic: bold = False


@dataclasses.dataclass
class BufferConsole:
    matrix: typing.List[typing.List[BufferCharacter]]
    shape: Cursor = Cursor(*DEFAULT_SIZE)
    cursor: Cursor = Cursor(0, 0)
    background: str = 'black'
    foreign: str = 'white'
    bold: bool = False
    italic: bold = False
    background_buffer: str = 'black'


empty_array2d = lambda size: zero_array2d(*size, BufferCharacter())

console = BufferConsole(matrix=empty_array2d(DEFAULT_SIZE))
keys_pressed = collections.deque()


def italichigh():
    console.italic = True


def italiclow():
    console.italic = False


def highvideo():
    console.bold = True


def lowvideo():
    console.bold = False


def reset():
    console.background = 'black'
    console.foreign = 'white'


def resize(columns, rows) -> None:
    console.shape = Cursor(columns, rows)
    console.matrix = memset_array2d(console.matrix, empty_array2d(tuple(console.shape)))


def clreol() -> None: ...


def clrscr():
    console.matrix = empty_array2d(tuple(console.shape))


def textbackground(color):
    console.background = color


def textcolor(color):
    console.foreign = color


def wherex():
    return tuple(console.cursor)[0]


def wherey():
    return tuple(console.cursor)[1]


def gotoxy(x, y):
    console.cursor = [x, y]


def putchxy(x, y, _chr):
    try:
        console.matrix[y][x] = BufferCharacter(_chr, console.background, console.foreign, bold=console.bold,
                                               italic=console.italic)
    except IndexError:
        pass


def kbhit():
    if len(keys_pressed) <= 0:
        return ''

    return keys_pressed.pop()


def getch():
    k = kbhit()

    while k == '':
        k = kbhit()

    return k


def getche():
    _chr = getch()
    console.matrix[wherey()][wherex()].char = _chr
    return _chr


def cputsxy(x, y, _str):
    for _chr in _str:
        putchxy(x, y, _chr)
        x += 1


def getbuffersize():
    return tuple(console.shape)


def scalewindow(scale): ...


def titlewindow(title) -> None:
    console.matrix.title = title


def refresh(): ...


def gettextinfo(): ...


def inittextinfo(): ...


def delline(): ...


def insline(): ...


def _conio_gettext(left, top, right, bottom, char_info): ...


def puttext(left, top, right, bottom): ...


def movetext(left, top, right, bottom, destleft, desttop): ...


def _setcursortype(type) -> None: ...


def textattr(attr) -> None: ...


def normvideo(): ...


def getpass(prompt, _str): ...


def delay(ms):
    pygame.time.delay(ms)


def switchbackground(color):
    console.background_buffer = color


def flashbackground(color, ms): ...


def clearkeybuf(): ...


def printf(_str, *args, **kwargs):
    cputsxy(wherex(), wherey(), _str)


def set_main_loop_thread(target):
    DEFAULT_FONT_NAME = "ModernDOS8x16.ttf"
    FRAMERATE_LIMIT = 30
    WINDOW_SIZE = 640, 480
    WINDOW_FLAGS = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE

    running = True

    def inner_target():
        nonlocal running

        try:
            target()
        except Exception as e:
            running = False
            raise e

    pygame.init()

    font = pygame.font.Font(DEFAULT_FONT_NAME, 16)
    screen = pygame.display.set_mode(WINDOW_SIZE, WINDOW_FLAGS)
    clock = pygame.time.Clock()

    thread = threading.Thread(target=inner_target)
    thread.daemon = True
    thread.start()

    size = font.render(' ', True, (0, 0, 0)).get_size()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), WINDOW_FLAGS)
                resize(event.w // size[0], event.h // size[1])

        keys = pygame.key.get_pressed()

        if len(keys_pressed) != 0:
            keys_pressed.clear()

        for i in range(len(keys)):
            if keys[i]:
                keys_pressed.appendleft(chr(i))

        screen.fill(pygame.Color(console.background_buffer))

        for y, row in enumerate(console.matrix):
            for x, _chr in enumerate(row):
                if _chr.char in ['']:
                    continue

                font.set_bold(_chr.bold)
                font.set_italic(_chr.italic)
                surface_chr = font.render(_chr.char, True, pygame.Color(_chr.foreign))

                surface = pygame.Surface(surface_chr.get_size())
                surface.fill(pygame.Color(_chr.background))
                surface.blit(surface_chr, (0, 0))

                screen.blit(surface, (x * size[0], y * size[1]))

        pygame.display.update()
        clock.tick(FRAMERATE_LIMIT)

    pygame.quit()


def set_main_loop(target):
    pass

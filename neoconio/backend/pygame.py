import collections
import threading
import typing

import pygame

import neoconio.abc.console
import neoconio.abc.thread_safe_console


class PygameConsole(neoconio.abc.thread_safe_console.ThreadSafeConsole):
    LIMIT_FRAMERATE = 60
    DEFAULT_FLAGS = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE

    def __init__(self, *args, **kwargs):
        super(PygameConsole, self).__init__(*args, **kwargs)
        self.__keys = collections.deque()

    def main_loop(self, target):
        running = True

        def inner_loop():
            nonlocal running, target

            try:
                target()
            except Exception as e:
                running = False
                raise e from e

        def init_font_map(filename):
            default_color = pygame.Color('white')
            default_size = 16

            if filename == "":
                raise f"Invalid filename: '{filename}'"

            font = pygame.font.Font(filename, default_size)
            size = 0, 0
            map_chr = {}

            for i in range(neoconio.abc.console.Console.U_CHR_MAX):
                try:
                    surface = font.render(chr(i), True, default_color)
                    map_chr[chr(i)] = surface
                    size = surface.get_size()
                except (ValueError, pygame.error):
                    pass

            return map_chr, size

        pygame.init()

        screen = pygame.display.set_mode(neoconio.abc.console.Console.DEFAULT_SIZE, PygameConsole.DEFAULT_FLAGS)
        clock = pygame.time.Clock()

        f_thread_loop = threading.Thread(target=inner_loop)
        f_thread_loop.daemon = True
        f_thread_loop.start()

        map_chr, size = init_font_map(self.filename_font)

        while running:
            pygame.display.set_caption(self.title)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode((event.w, event.h), PygameConsole.DEFAULT_FLAGS)
                    self.resize(event.w // size[0], event.h // size[0])

                if self.runtime:
                    self.runtime.event(event)

            keys = pygame.key.get_pressed()

            if len(self.__keys) != 0:
                self.__keys.clear()

            for i in range(len(keys)):
                if keys[i]:
                    self.__keys.appendleft(chr(i))

            if self.runtime:
                self.runtime.update()

            screen.fill((0, 0, 0))

            for y, row in enumerate(self.matrix):
                for x, _chr in enumerate(row):
                    if _chr in map_chr.keys():
                        if _chr in [' ', '']:
                            continue

                        surface = map_chr[_chr]
                        screen.blit(surface, (x * surface.get_width(), y * surface.get_height()))

            if self.runtime:
                self.runtime.render(screen)

            pygame.display.flip()
            clock.tick(PygameConsole.LIMIT_FRAMERATE)

        pygame.quit()

    def kbhit(self) -> chr:
        if len(self.__keys) <= 0:
            return ''

        return self.__keys.pop()

    def getch(self) -> chr:
        k = self.kbhit()

        while k == '':
            k = self.kbhit()

        return k

    def getche(self) -> chr:
        _chr = self.getch()
        self.matrix[self.wherey()][self.wherex()] = _chr
        return _chr

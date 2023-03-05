import collections
import threading

import pygame

import neoconio.abc.thread_safe_console
import neoconio.abc.console


class PygameConsole(neoconio.abc.thread_safe_console.ThreadSafeConsole):
    LIMIT_FRAMERATE = 30

    def __init__(self, *args, **kwargs):
        super(PygameConsole, self).__init__(*args, **kwargs)
        self.__keys = collections.deque()
        self.__lock = threading.Condition()

    def main_loop(self, target):
        running = True

        def init_font_map(filename):
            if filename == "":
                raise f"Invalid filename: '{filename}'"

            font = pygame.font.Font(filename, 16)
            map_chr_surface = {}

            for i in range(neoconio.abc.console.Console.U_CHR_MAX):
                try:
                    map_chr_surface[chr(i)] = font.render(chr(i), True, pygame.Color('white'))
                except Exception as e:
                    pass

            return font, map_chr_surface

        pygame.init()

        screen = pygame.display.set_mode(neoconio.abc.console.Console.DEFAULT_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
        clock = pygame.time.Clock()

        f_thread_loop = threading.Thread(target=target)
        f_thread_loop.daemon = True
        f_thread_loop.start()

        font, matrix_map_chr = init_font_map(self.filename_font)

        while running:
            pygame.display.set_caption(self.title)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                if self.runtime:
                    self.runtime.event(event)

            keys = pygame.key.get_pressed()

            for i in range(len(keys)):
                if keys[i]:
                    self.__keys.appendleft(chr(i))

            if self.runtime:
                self.runtime.update()

            screen.fill((0, 0, 0))

            x, y = 0, 0
            for c, surface in matrix_map_chr.items():
                if surface is not None:
                    screen.blit(surface, (x, y))
                    x += surface.get_width()

                    if x >= screen.get_width():
                        x = 0
                        y += surface.get_height()

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
        return self.getch()

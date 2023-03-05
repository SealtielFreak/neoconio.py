import threading
import typing

import pygame

from neoconio.abc.console import Console


class PygameConsole(Console):
    LIMIT_FRAMERATE = 30

    def __init__(self, *args, **kwargs):
        super(PygameConsole, self).__init__(*args, **kwargs)
        self.__lock = threading.Condition()

    def main_loop(self, target):
        running = True

        def init_font_map(filename):
            if filename == "":
                raise f"Invalid filename: '{filename}'"
            
            font = pygame.font.Font(filename, 16)
            matrix_map_chr = [None] * Console.U_CHR_MAX

            for i, c in enumerate(matrix_map_chr):
                try:
                    matrix_map_chr[i] = font.render(chr(i), True, pygame.Color('white'))
                except Exception as e:
                    pass

            return font, matrix_map_chr

        pygame.init()

        screen = pygame.display.set_mode(Console.DEFAULT_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
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
            
            if self.runtime:
                self.runtime.update()

            screen.fill((0, 0, 0))

            x, y = 0, 0
            for surface in matrix_map_chr:
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

try:
    import pygame
    from neoconio.backend.pygame import PygameConsole as Console

except ImportError as e:
    import pysdl2
    from neoconio.backend.sdl2 import SDLConsole as Console

__all__ = ["Console"]

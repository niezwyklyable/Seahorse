import pygame
from .constants import WHITE, LAYER_1, LAYER_2, LAYER_3, LAYER_4 

class Game():
    def __init__(self, win):
        self.win = win

    def render(self):
        # background
        self.win.fill(WHITE)
        self.win.blit(LAYER_1, (0, 0))
        self.win.blit(LAYER_2, (0, 0))
        self.win.blit(LAYER_3, (0, 0))
        self.win.blit(LAYER_4, (0, 0))

        pygame.display.update()

    def update(self):
        pass

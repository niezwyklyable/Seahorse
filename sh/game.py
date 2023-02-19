import pygame
from .constants import WHITE, LAYER_1, LAYER_2, LAYER_3, LAYER_4
from .player import Player

class Game():
    def __init__(self, win):
        self.win = win
        self.player = None
        self.create_player()

    def render(self):
        # background
        self.win.fill(WHITE)
        # self.win.blit(LAYER_1, (0, 0))
        # self.win.blit(LAYER_2, (0, 0))
        # self.win.blit(LAYER_3, (0, 0))
        # self.win.blit(LAYER_4, (0, 0))

        # player
        if self.player:
            self.player.draw(self.win)

        pygame.display.update()

    def update(self):
        self.player.change_state()

    def create_player(self):
        self.player = Player(100, 250)

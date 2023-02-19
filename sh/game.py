import pygame
from .constants import WHITE, BACKGROUND
from .player import Player

class Game():
    def __init__(self, win):
        self.win = win
        self.player = None
        self.create_player()
        
    def render(self):
        # background
        self.win.fill(WHITE)
        self.win.blit(BACKGROUND, (0, 0))

        # player
        if self.player:
            self.player.draw(self.win)

        pygame.display.update()

    def update(self):
        self.player.change_state()

    def create_player(self):
        self.player = Player(100, 250)

import pygame
from .constants import WHITE, BACKGROUND, WIDTH
from .player import Player

class Game():
    def __init__(self, win):
        self.win = win
        self.player = None
        self.create_player()
        self.bg1_x = 0
        self.bg2_x = BACKGROUND.get_width()
        
    def render(self):
        # background
        self.win.fill(WHITE)
        self.bg1_x -= 1
        self.bg2_x -= 1
        self.win.blit(BACKGROUND, (self.bg1_x, 0)) # first background
        self.win.blit(BACKGROUND, (self.bg2_x, 0)) # second background
        if self.bg1_x <= -2*BACKGROUND.get_width() + WIDTH:
            self.bg1_x = WIDTH
        if self.bg2_x <= -BACKGROUND.get_width():
            self.bg2_x = BACKGROUND.get_width()

        # player
        if self.player:
            self.player.draw(self.win)

        pygame.display.update()

    def update(self):
        self.player.change_state()

    def create_player(self):
        self.player = Player(100, 250)

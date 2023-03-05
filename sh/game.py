import pygame
from .constants import WHITE, BACKGROUND, WIDTH, BOTTOM_BOUNDARY, UPPER_BOUNDARY, \
    ANGLER_LIST, DIM_FACTOR
from .player import Player
from .angler import Angler
import random

class Game():
    def __init__(self, win):
        self.win = win
        self.player = None
        self.angler = None
        self.create_player()
        self.create_angler()
        self.bg1_x = 0
        self.bg2_x = BACKGROUND.get_width()
        
    def update(self):
        # player
        if self.player:
            self.player.change_state()
            # projectiles
            if self.player.projectiles:
                for p in self.player.projectiles:
                    if p.x > WIDTH + p.IMG.get_width()//2:
                        self.player.projectiles.remove(p) # delete if it is out of screen
                    elif self.collision_detection(p, self.angler): # check if it is collision with an angler
                        self.player.projectiles.remove(p) # delete projectile because it exploded
                        self.create_angler() # angler is dead so create a new one
                    else:
                        p.move()
        
        # angler
        if self.angler:
            self.angler.change_state()
            self.angler.move()
            # restart if it is out of screen
            if self.angler.x < 0 - self.angler.IMG.get_width()//2:
                self.create_angler()

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
            # projectiles
            if self.player.projectiles:
                for p in self.player.projectiles:
                    p.draw(self.win)

        # angler
        if self.angler:
            self.angler.draw(self.win)

        pygame.display.update()

    def create_player(self):
        self.player = Player(100, 250)

    def create_angler(self):
        RANDOM_Y = random.choice(range(UPPER_BOUNDARY+ANGLER_LIST[0].get_height()//2, \
            BOTTOM_BOUNDARY-ANGLER_LIST[0].get_height()//2+5,\
            5))
        self.angler = Angler(WIDTH+ANGLER_LIST[0].get_width()//2,\
                                RANDOM_Y)
        
    def collision_detection(self, obj1, obj2):
        if obj1.TYPE == 'PROJECTILE' and obj2.TYPE == 'ANGLER':
            # check distances between positions of two objects in a range of the bigger object
            if abs(obj1.x - obj2.x) <= obj2.IMG.get_width()//2*DIM_FACTOR and \
                abs(obj1.y - obj2.y) <= obj2.IMG.get_height()//2*DIM_FACTOR:
                return True
            
        return False

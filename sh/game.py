import pygame
from .constants import WHITE, BACKGROUND, WIDTH, BOTTOM_BOUNDARY, UPPER_BOUNDARY, \
    ANGLER_LIST, DIM_FACTOR
from .player import Player
from .angler import Angler
import random
from .explosions import SmokeExplosion, FireExplosion

class Game():
    def __init__(self, win):
        self.win = win
        self.player = None
        self.anglers = []
        self.explosions = []
        self.create_player()
        self.create_angler()
        self.bg1_x = 0
        self.bg2_x = BACKGROUND.get_width()
        
    def update(self):
        # player
        if self.player:
            self.player.change_state()
            # projectiles
            for p in self.player.projectiles:
                if p.x > WIDTH + p.IMG.get_width()//2:
                    self.player.projectiles.remove(p) # delete if it is out of screen
                    continue
                for a in self.anglers:
                    if self.collision_detection(p, a): # check if it is collision with an angler
                        self.player.projectiles.remove(p) # delete projectile after collision
                        self.initiate_explosion(a.x, a.y) # initiate smoke or fire explosion
                        self.anglers.remove(a) # delete angler because it exploded
                        self.create_angler() # DELETE THIS LINE AFTER DEVELOPING RANDOM FISH CREATING
                else:
                    p.move()
        
        # anglers
        for a in self.anglers:
            a.change_state()
            a.move()
            # delete if it is out of screen
            if a.x < 0 - a.IMG.get_width()//2:
                self.anglers.remove(a)
                self.create_angler() # DELETE THIS LINE AFTER DEVELOPING RANDOM FISH CREATING

        # explosions
        for e in self.explosions:
            if e.counter < len(e.IMG_TUPLE) - 1:
                e.change_state()
            else:
                self.explosions.remove(e) # delete an explosion from the list if it ends its animation

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
            for p in self.player.projectiles:
                p.draw(self.win)

        # anglers
        for a in self.anglers:
            a.draw(self.win)

        # explosions
        for e in self.explosions:
            e.draw(self.win)

        pygame.display.update()

    def create_player(self):
        self.player = Player(100, 250)

    def create_angler(self):
        RANDOM_Y = random.choice(range(UPPER_BOUNDARY+ANGLER_LIST[0].get_height()//2, \
            BOTTOM_BOUNDARY-ANGLER_LIST[0].get_height()//2+5,\
            5))
        self.anglers.append(Angler(WIDTH+ANGLER_LIST[0].get_width()//2,\
                                RANDOM_Y))
        
    # initiate an explosion after some fish died
    def initiate_explosion(self, x, y):
        if random.choice(range(10)) < 5: # 50% probability
            self.explosions.append(SmokeExplosion(x, y))
        else:
            self.explosions.append(FireExplosion(x, y))
        
    def collision_detection(self, obj1, obj2):
        if obj1.TYPE == 'PROJECTILE' and obj2.TYPE == 'ANGLER':
            # check distances between positions of two objects in a range of the bigger object
            if abs(obj1.x - obj2.x) <= obj2.IMG.get_width()//2*DIM_FACTOR and \
                abs(obj1.y - obj2.y) <= obj2.IMG.get_height()//2*DIM_FACTOR:
                return True
            
        return False

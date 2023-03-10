import pygame
from .constants import WHITE, BACKGROUND, WIDTH, BOTTOM_BOUNDARY, UPPER_BOUNDARY, \
    ANGLER_LIST, DIM_FACTOR, DRONE_LIST, HIVEWHALE_LIST, LUCKY_LIST, FPS, FISH_CALLING_FREQUENCY_FACTOR
from .player import Player
from .enemies import Angler, Drone, Hivewhale, Lucky
import random
from .explosions import SmokeExplosion, FireExplosion

class Game():
    def __init__(self, win):
        self.win = win
        self.player = None
        self.enemies = []
        self.explosions = []
        self.create_player()
        self.bg1_x = 0
        self.bg2_x = BACKGROUND.get_width()
        self.frames = 0 # it is responsible for current time in the game (frames / fps = time [s])
        self.frames_to_load_projectile = 0 # it is linked with const FRAMES_TO_LOAD_PROJECTILE_THRESHOLD
        
    def update(self):
        # current time
        self.frames += 1

        # time to load the projectile to launch it
        self.frames_to_load_projectile += 1

        # cyclic randomize with creating enemies
        if FISH_CALLING_FREQUENCY_FACTOR * self.frames % FPS == 0:
            print('seconds: ' + str(self.frames / FPS))
            RANDOM_FISH = random.choice(range(4))
            if RANDOM_FISH == 0:
                self.create_angler()
            elif RANDOM_FISH == 1:
                self.create_drone()
            elif RANDOM_FISH == 2:
                self.create_hivewhale()
            else:
                self.create_lucky()
            
            print('number of enemies: ' + str(len(self.enemies)))
            #print('number of projectiles: ' + str(len(self.player.projectiles)))

        # player
        if self.player:
            self.player.change_state()
            # projectiles
            for p in self.player.projectiles:
                if p.x > WIDTH + p.IMG.get_width()//2:
                    self.player.projectiles.remove(p) # delete if it is out of screen
                    continue
                for e in self.enemies:
                    if self.collision_detection(p, e): # check if it is collision with an enemy
                        self.player.projectiles.remove(p) # delete projectile after collision
                        self.initiate_explosion(e.x, e.y) # initiate smoke or fire explosion
                        self.enemies.remove(e) # delete the enemy because it exploded
                        break
                else:
                    p.move()
        
        # enemies
        for e in self.enemies:
            e.change_state()
            e.move()
            # delete if it is out of screen
            if e.x < 0 - e.IMG.get_width()//2:
                self.enemies.remove(e)

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

        # enemies
        for e in self.enemies:
            e.draw(self.win)

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
        self.enemies.append(Angler(WIDTH+ANGLER_LIST[0].get_width()//2,\
                                RANDOM_Y))
        
    def create_drone(self):
        RANDOM_Y = random.choice(range(UPPER_BOUNDARY+DRONE_LIST[0].get_height()//2, \
            BOTTOM_BOUNDARY-DRONE_LIST[0].get_height()//2+5,\
            5))
        self.enemies.append(Drone(WIDTH+DRONE_LIST[0].get_width()//2,\
                                RANDOM_Y))
        
    def create_hivewhale(self):
        RANDOM_Y = random.choice(range(UPPER_BOUNDARY+HIVEWHALE_LIST[0].get_height()//2, \
            BOTTOM_BOUNDARY-HIVEWHALE_LIST[0].get_height()//2+5,\
            5))
        self.enemies.append(Hivewhale(WIDTH+HIVEWHALE_LIST[0].get_width()//2,\
                                RANDOM_Y))
        
    def create_lucky(self):
        RANDOM_Y = random.choice(range(UPPER_BOUNDARY+LUCKY_LIST[0].get_height()//2, \
            BOTTOM_BOUNDARY-LUCKY_LIST[0].get_height()//2+5,\
            5))
        self.enemies.append(Lucky(WIDTH+LUCKY_LIST[0].get_width()//2,\
                                RANDOM_Y))
        
    # initiate an explosion after some fish died
    def initiate_explosion(self, x, y):
        if random.choice(range(10)) < 5: # 50% probability
            self.explosions.append(SmokeExplosion(x, y))
        else:
            self.explosions.append(FireExplosion(x, y))
        
    def collision_detection(self, obj1, obj2):
        if obj1.TYPE == 'PROJECTILE' and (obj2.TYPE == 'ANGLER' or obj2.TYPE == 'DRONE'\
                or obj2.TYPE == 'LUCKY'):
            # check distances between positions of two objects in a range of the bigger object
            if abs(obj1.x - obj2.x) <= obj2.IMG.get_width()//2*DIM_FACTOR and \
                abs(obj1.y - obj2.y) <= obj2.IMG.get_height()//2*DIM_FACTOR:
                return True
            
        if obj1.TYPE == 'PROJECTILE' and obj2.TYPE == 'HIVEWHALE':
            # check distances between positions of two objects in a range of the bigger object
            if abs(obj1.x - obj2.x) <= obj2.IMG.get_width()//2 and \
                abs(obj1.y - obj2.y) <= obj2.IMG.get_height()//2:
                return True
            
        return False

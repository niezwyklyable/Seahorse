import pygame
from .constants import WHITE, BACKGROUND, WIDTH, BOTTOM_BOUNDARY, UPPER_BOUNDARY, \
    ANGLER_LIST, DIM_FACTOR, DRONE_LIST, HIVEWHALE_LIST, LUCKY_LIST, FPS, FISH_CALLING_FREQUENCY_FACTOR, \
    LUCKY_FISH_PERCENTAGE, DOUBLE_SHOOTING_FRAMES_THRESHOLD, PLAY_TIME, SCORE_GOAL, BLACK, HEIGHT, \
    NUM_OF_GEARS, BOUNCING_THRESHOLD
from .player import Player
from .enemies import Angler, Drone, Hivewhale, Lucky
import random
from .explosions import SmokeExplosion, FireExplosion
from .gears import Gear
import pymunk

class Game():
    def __init__(self, win, space, draw_options):
        self.win = win
        self.player = None
        self.enemies = []
        self.explosions = []
        self.gears = []
        self.create_player()
        self.bg1_x = 0
        self.bg2_x = BACKGROUND.get_width()
        self.frames = 0 # it is responsible for current time in the game (frames / fps = time [s])
        self.frames_to_load_projectile = 0 # it is linked with const FRAMES_TO_LOAD_PROJECTILE_THRESHOLD
        self.frames_to_change_mode = 0 # it is linked with const DOUBLE_SHOOTING_FRAMES_THRESHOLD
        self.score = 0
        self.gameover = False # it disables some things after the end of the game
        self.text1 = '' # it contains info about game score and appears on the screen all the time
        self.text2 = '' # it contains info about time to left and appears on the screen all the time
        self.msg = '' # the message that will show on the center of the screen after the end of the game
        self.space = space # pymunk stuff (virtual environment)
        self.draw_options = draw_options # pymunk stuff (responsible for rendering objects in the space)
        self.create_floor() # pymunk stuff (creating a rectangular shape needed for bouncing effects)

    def update(self):
        # current time
        self.frames += 1

        # time to load the projectile to launch it
        self.frames_to_load_projectile += 1

        # cyclic randomize with creating enemies
        if FISH_CALLING_FREQUENCY_FACTOR * self.frames % FPS == 0:
            RANDOM_FISH = random.choice(range(100))
            if RANDOM_FISH in range(LUCKY_FISH_PERCENTAGE):
                self.create_lucky()
            else:
                RANDOM_FISH = random.choice(range(3))
                if RANDOM_FISH == 0:
                    self.create_angler()
                elif RANDOM_FISH == 1:
                    self.create_drone()
                else:
                    self.create_hivewhale()

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
                        if e.TYPE == 'HIVEWHALE':
                            e.lives -= 1
                            if e.lives > 0:
                                break
                        self.initiate_explosion(e.x, e.y) # initiate smoke or fire explosion
                        self.create_gears(e.x, e.y)
                        if e.TYPE == 'HIVEWHALE':
                            self.create_4_drones(e.x, e.y, e.IMG) # create 4 drones after Hivewhale's death
                        self.score += e.reward # add points to score for killing an enemy
                        self.enemies.remove(e) # delete the enemy because it exploded
                        break
                else:
                    p.move()

            # change Player's mode from double shooting to single shooting
            if self.player.double_shooting_mode:
                self.frames_to_change_mode += 1 # update bonus time
                if self.frames_to_change_mode >= DOUBLE_SHOOTING_FRAMES_THRESHOLD:
                    self.player.change_mode_to_single_shooting()    

        # enemies
        for e in self.enemies:
            if not self.gameover and self.collision_detection(self.player, e):
                if e.TYPE == 'LUCKY': # lucky fish collision effect
                    if not self.player.double_shooting_mode:
                        self.player.change_mode_to_double_shooting() # change Player mode to double shooting
                    self.frames_to_change_mode = 0 # reset time of the bonus
                else: # every other fish type effect
                    self.score -= 1
                self.enemies.remove(e) # delete the fish because it interacted with the Player
                continue
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

        # gears
        for g in self.gears:
            if not g.removed_from_space:
                # passing coordinates from the space to the real x, y coords of the gears
                g.x = g.body.position[0]
                g.y = g.body.position[1]
                # check collision with the floor (limited bouncing effect)
                if g.y >= HEIGHT-50 - g.IMG.get_height()//2:
                    g.body.position = (g.x, HEIGHT-50 - g.IMG.get_height()//2) # thanks to this alignment, the gear does not stuck in above condition (does bouncing)
                    g.bounce_counter += 1
                    # remove the gear from the space after a few bounces but do not delete the gear itself yet
                    if g.bounce_counter >= BOUNCING_THRESHOLD:
                        self.space.remove(g.shape, g.body)
                        g.removed_from_space = True
            else:
                g.move() # it will be falling until it is out of screen

            # delete if it is out of screen
            if g.y > HEIGHT + g.IMG.get_height()//2:
                self.gears.remove(g)

        # score and time info
        if not self.gameover:
            font = pygame.font.SysFont('comicsans', 30)
            self.text1 = font.render(f'Score: {self.score}/{SCORE_GOAL}', 1, WHITE)
            self.text2 = font.render('Time to left: {:.1f}s'.format(PLAY_TIME-self.frames/FPS), 1, WHITE)
        
        # win and lose conditions
        if not self.gameover and self.frames / FPS >= PLAY_TIME:
            self.gameover = True
            font = pygame.font.SysFont('comicsans', 40)
            if self.score >= SCORE_GOAL:
                self.msg = font.render(f'YOU WON!, YOUR SCORE: {self.score}/{SCORE_GOAL}',\
                                    1, WHITE, BLACK)
            else:
                self.msg = font.render(f'YOU LOST!, YOUR SCORE: {self.score}/{SCORE_GOAL}',\
                                    1, WHITE, BLACK)

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

        # gears
        for g in self.gears:
            g.draw(self.win)

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

        # verbose
        self.show_info()

        #self.space.debug_draw(self.draw_options) # temporarily visualization objects from the space
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
        
    def create_4_drones(self, x, y, img):
        x1 = x + img.get_width()//4
        y1 = y + img.get_height()//4
        y2 = y - img.get_height()//4
        self.enemies.append(Drone(x1, y1))
        self.enemies.append(Drone(x1, y2))
        self.enemies.append(Drone(x, y1))
        self.enemies.append(Drone(x, y2))

    def create_gears(self, x, y):
        for _ in range(NUM_OF_GEARS):
            self.gears.append(Gear(x, y, self.space))

    # an invisible rectangle at the bottom of the screen which collides with the gears and makes them bounce
    def create_floor(self):
        body = pymunk.Body(body_type=pymunk.Body.STATIC) # static body does not have mass
        body.position = (WIDTH//2, HEIGHT-50//2) # central pos x and y
        shape = pymunk.Poly.create_box(body, (WIDTH, 50)) # a rectangle with w and h dims
        shape.color = (255, 0, 0, 100) # if not specified it is just grey
        shape.elasticity = 0.4
        shape.friction = 0.5
        self.space.add(body, shape)

    def show_info(self):
        self.win.blit(self.text1, (20, HEIGHT-self.text1.get_height()))
        self.win.blit(self.text2, (300, HEIGHT-self.text1.get_height()))

        if self.gameover:
            self.win.blit(self.msg, (int(WIDTH/2 - self.msg.get_width()/2), \
                int(HEIGHT/2 - self.msg.get_height()/2)))

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
            
        if obj1.TYPE == 'PLAYER' and (obj2.TYPE == 'LUCKY' or obj2.TYPE == 'ANGLER' or obj2.TYPE == 'DRONE'):
            # check distances between positions of two objects in a range of both objects
            if abs(obj1.x - obj2.x) <= (obj1.IMG.get_width()//2 + obj2.IMG.get_width()//2)*DIM_FACTOR and \
                abs(obj1.y - obj2.y) <= (obj1.IMG.get_height()//2 + obj2.IMG.get_height()//2)*DIM_FACTOR:
                return True
            
        if obj1.TYPE == 'PLAYER' and obj2.TYPE == 'HIVEWHALE':
            # check distances between positions of two objects in a range of both objects
            if abs(obj1.x - obj2.x) <= obj1.IMG.get_width()//2*DIM_FACTOR + obj2.IMG.get_width()//2 and \
                abs(obj1.y - obj2.y) <= obj1.IMG.get_height()//2*DIM_FACTOR + obj2.IMG.get_height()//2:
                return True
            
        return False

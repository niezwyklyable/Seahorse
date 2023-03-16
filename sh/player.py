from .sprite import Sprite
from .constants import PLAYER_LIST, UPPER_BOUNDARY, BOTTOM_BOUNDARY, PLAYER_2_LIST
from .projectile import Projectile

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=PLAYER_LIST, TYPE='PLAYER', x=x, y=y)
        self.dY = 5
        self.projectiles = []
        self.double_shooting_mode = False
        #self.change_mode_to_double_shooting()

    # steering
    def move(self, dir):
        if dir == 'up':
            self.y -= self.dY
            # check boundaries
            if self.y < UPPER_BOUNDARY + self.IMG.get_height()//2:
                self.y = UPPER_BOUNDARY + self.IMG.get_height()//2
        elif dir == 'down':
            self.y += self.dY
            # check boundaries
            if self.y > BOTTOM_BOUNDARY - self.IMG.get_height()//2:
                self.y = BOTTOM_BOUNDARY - self.IMG.get_height()//2
            
    def launch_projectile(self):
        if self.double_shooting_mode:
            self.projectiles.append(Projectile(self.x + 138-100, self.y + 187-250)) # from the nose
            self.projectiles.append(Projectile(self.x + 144-100, self.y + 334-250)) # from the tail
        else:
            # single shooting (from the nose only)
            self.projectiles.append(Projectile(self.x + 138-100, self.y + 187-250))

    def change_mode_to_double_shooting(self):
        self.IMG_TUPLE = tuple(PLAYER_2_LIST)
        self.IMG = self.IMG_TUPLE[self.counter]
        self.double_shooting_mode = True

    def change_mode_to_single_shooting(self):
        self.IMG_TUPLE = tuple(PLAYER_LIST)
        self.IMG = self.IMG_TUPLE[self.counter]
        self.double_shooting_mode = False

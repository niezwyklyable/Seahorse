from .sprite import Sprite
from .constants import PLAYER_LIST, UPPER_BOUNDARY, BOTTOM_BOUNDARY

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=PLAYER_LIST, TYPE='PLAYER', x=x, y=y)
        self.dY = 5

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
            

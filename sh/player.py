from .sprite import Sprite
from .constants import SH, UPPER_BOUNDARY, BOTTOM_BOUNDARY

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG=SH[0], TYPE='PLAYER', x=x, y=y)
        self.IMG_TUPLE = tuple(SH)
        self.counter = 0
        self.dY = 5

    # animation changing
    def change_state(self):
        self.counter += 1
        if self.counter < len(self.IMG_TUPLE):
            self.IMG = self.IMG_TUPLE[self.counter]
        else:
            self.counter = 0
            self.IMG = self.IMG_TUPLE[0]

    # steering
    def move(self, dir):
        if dir == 'up':
            self.y -= self.dY
            # check boundaries
            if self.y < UPPER_BOUNDARY:
                self.y = UPPER_BOUNDARY
        elif dir == 'down':
            self.y += self.dY
            # check boundaries
            if self.y > BOTTOM_BOUNDARY:
                self.y = BOTTOM_BOUNDARY
            

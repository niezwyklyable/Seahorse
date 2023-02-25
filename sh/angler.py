from .sprite import Sprite
from .constants import ANGLER_1_STATE_1_LIST

class Angler_1(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG=ANGLER_1_STATE_1_LIST[0], TYPE='ANGLER_1', x=x, y=y)
        self.IMG_TUPLE = tuple(ANGLER_1_STATE_1_LIST)
        self.counter = 0
        self.dX = 2

    # animation changing
    def change_state(self):
        self.counter += 1
        if self.counter < len(self.IMG_TUPLE):
            self.IMG = self.IMG_TUPLE[self.counter]
        else:
            self.counter = 0
            self.IMG = self.IMG_TUPLE[0]
    
    # movement
    def move(self):
        self.x -= self.dX

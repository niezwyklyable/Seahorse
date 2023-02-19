from .sprite import Sprite
from .constants import SH

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG=SH[0], TYPE='PLAYER', x=x, y=y)
        self.IMG_TUPLE = tuple(SH)
        self.counter = 0

    # animation changing
    def change_state(self):
        self.counter += 1
        if self.counter < len(self.IMG_TUPLE):
            self.IMG = self.IMG_TUPLE[self.counter]
        else:
            self.counter = 0
            self.IMG = self.IMG_TUPLE[0]
            
from .sprite import Sprite
from .constants import GEARS_LIST
import random

class Gear(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=GEARS_LIST, TYPE='GEAR', x=x, y=y)
        self.randomize_asset()

    def change_state(self):
        print('there is no animation for this class')

    def move(self):
        print('there is no move for this class')

    def randomize_asset(self):
        self.IMG = random.choice(self.IMG_TUPLE)

from .sprite import Sprite
from .constants import ANGLER_LIST

class Angler(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=ANGLER_LIST, TYPE='ANGLER', x=x, y=y)
        self.dX = 2
    
    # movement
    def move(self):
        self.x -= self.dX

from .sprite import Sprite
from .constants import PROJECTILE

class Projectile(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=[PROJECTILE], TYPE='PROJECTILE', x=x, y=y)
        self.dX = 8

    def change_state(self):
        print('there is no animation for this class')

    def move(self):
        self.x += self.dX

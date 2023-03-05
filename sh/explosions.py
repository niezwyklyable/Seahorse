from .sprite import Sprite
from .constants import FIRE_EXPLOSION_LIST, SMOKE_EXPLOSION_LIST

class FireExplosion(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=FIRE_EXPLOSION_LIST, TYPE='EXPLOSION', x=x, y=y)

class SmokeExplosion(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=SMOKE_EXPLOSION_LIST, TYPE='EXPLOSION', x=x, y=y)
        
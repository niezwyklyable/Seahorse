from .sprite import Sprite
from .constants import SH

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG=SH[0], TYPE='PLAYER', x=x, y=y)
        
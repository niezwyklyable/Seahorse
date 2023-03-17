from .sprite import Sprite
from .constants import ANGLER_LIST, DRONE_LIST, HIVEWHALE_LIST, LUCKY_LIST

class Angler(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=ANGLER_LIST, TYPE='ANGLER', x=x, y=y)
        self.dX = 2
        self.reward = 1
    
    # movement
    def move(self):
        self.x -= self.dX

class Drone(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=DRONE_LIST, TYPE='DRONE', x=x, y=y)
        self.dX = 4
        self.reward = 2
    
    # movement
    def move(self):
        self.x -= self.dX

class Hivewhale(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=HIVEWHALE_LIST, TYPE='HIVEWHALE', x=x, y=y)
        self.dX = 1
        self.lives = 4
        self.reward = 5
    
    # movement
    def move(self):
        self.x -= self.dX

class Lucky(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_LIST=LUCKY_LIST, TYPE='LUCKY', x=x, y=y)
        self.dX = 3
        self.reward = 1
    
    # movement
    def move(self):
        self.x -= self.dX

class Sprite(): # an abstract class
    def __init__(self, IMG_LIST, TYPE, x, y): # x, y - centre pos
        self.IMG_TUPLE = tuple(IMG_LIST)
        self.IMG = self.IMG_TUPLE[0]
        self.TYPE = TYPE
        self.x = x
        self.y = y
        self.counter = 0

    def draw(self, win):
        win.blit(self.IMG, (self.x - self.IMG.get_width() // 2, \
            self.y - self.IMG.get_height() // 2))
        
    # animation changing
    def change_state(self):
        self.counter += 1
        if self.counter < len(self.IMG_TUPLE):
            self.IMG = self.IMG_TUPLE[self.counter]
        else:
            self.counter = 0
            self.IMG = self.IMG_TUPLE[0]

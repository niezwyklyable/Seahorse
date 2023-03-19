from .sprite import Sprite
from .constants import GEARS_LIST
import random
import pymunk

class Gear(Sprite):
    def __init__(self, x, y, space):
        super().__init__(IMG_LIST=GEARS_LIST, TYPE='GEAR', x=x, y=y)
        self.randomize_asset()
        self.create_body_and_shape(space)
        self.bounce_counter = 0 # it counts how many times the gear was bounced from the floor
        self.removed_from_space = False # it prevents the bugg with removing something that was already removed
        self.dY = 4 # for falling effect only after removing from the space

    def change_state(self):
        print('there is no animation for this class')

    def move(self):
        self.y += self.dY

    def randomize_asset(self):
        self.IMG = random.choice(self.IMG_TUPLE)

    def create_body_and_shape(self, space):
        self.body = pymunk.Body()
        self.body.position = (self.x, self.y)
        self.shape = pymunk.Circle(self.body, self.IMG.get_width()//2) # a half of width or height is a radius of the single gear asset
        self.shape.color = (255, 255, 255, 100)
        self.shape.mass = 100
        self.shape.elasticity = 0.9
        self.shape.friction = 0.4
        space.add(self.body, self.shape)
        self.body.apply_impulse_at_local_point((-10000, -25000), (0, 0)) # force vector applies to the shape
            # force_x, force_y, force_local_pos_x, force_local_pos_y
            # warning: too high force values may cause a collision bugg
            # it strongly depends on mass value of the shape

from pygame.image import load
from pygame.transform import scale

# screen refreshing frequency
FPS = 30

# screen dims and scale
WIDTH, HEIGHT = 1500, 750
FACTOR = HEIGHT/500 # 500px is a non-sliding dim of background layers

# colors
WHITE = (255, 255, 255)

# background
LAYER_1 = scale(load('assets/layer1.png'), (FACTOR*1768, FACTOR*500))
LAYER_2 = scale(load('assets/layer2.png'), (FACTOR*1768, FACTOR*500))
LAYER_3 = scale(load('assets/layer3.png'), (FACTOR*1768, FACTOR*500))
LAYER_4 = scale(load('assets/layer4.png'), (FACTOR*1768, FACTOR*500))

# seahorse
PLAYER = load('assets/player.png')
SH = []
for i in range(4680//120):
    SH.append(scale(PLAYER.subsurface(i*120, 0, 120, 192), (FACTOR*120, FACTOR*192)))
    
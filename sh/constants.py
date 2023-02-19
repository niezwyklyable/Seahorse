from pygame.image import load
from pygame.transform import scale

# screen refreshing frequency
FPS = 60

# screen dims and scale
WIDTH, HEIGHT = 1000, 500

# colors
WHITE = (255, 255, 255)

# background
BACKGROUND = load('assets/background.png') # 1768x500px

# seahorse
PLAYER = load('assets/player.png')
SH = []
for i in range(4680//120):
    SH.append(PLAYER.subsurface(i*120, 0, 120, 192))
    
from pygame.image import load
#from pygame.transform import scale

# screen refreshing frequency
FPS = 60

# screen dims
WIDTH, HEIGHT = 1000, 500

# colors
WHITE = (255, 255, 255)

# boundaries
UPPER_BOUNDARY = 10
BOTTOM_BOUNDARY = 450

# background
BACKGROUND = load('assets/background.png') # 1768x500px

# seahorse
PLAYER = load('assets/player.png')
PLAYER_LIST = []
for i in range(4680//120):
    PLAYER_LIST.append(PLAYER.subsurface(i*120, 0, 120, 192))
    
# enemies
ANGLER = load('assets/angler1.png')
ANGLER_LIST = []
for i in range(8892//228):
    ANGLER_LIST.append(ANGLER.subsurface(i*228, 0, 228, 170))

# projectile
PROJECTILE = load('assets/projectile.png')

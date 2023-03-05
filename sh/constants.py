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

# factors
DIM_FACTOR = 0.8 # it decreases the base distance for collision detection method to make it more realistic and precisely
REPLICATE_FACTOR = 3 # it extends the lifetime of a single animation (positive int only)

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

# smoke explosion
SMOKE_EXPLOSION = load('assets/smokeExplosion.png')
SMOKE_EXPLOSION_LIST = []
for i in range(1600//200):
    for j in range(REPLICATE_FACTOR):
        SMOKE_EXPLOSION_LIST.append(SMOKE_EXPLOSION.subsurface(i*200, 0, 200, 200))

# fire explosion
FIRE_EXPLOSION = load('assets/fireExplosion.png')
FIRE_EXPLOSION_LIST = []
for i in range(1600//200):
    for j in range(REPLICATE_FACTOR):
        FIRE_EXPLOSION_LIST.append(FIRE_EXPLOSION.subsurface(i*200, 0, 200, 200))

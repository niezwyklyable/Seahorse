from pygame.image import load
#from pygame.transform import scale

# screen refreshing frequency
FPS = 60

# screen dims
WIDTH, HEIGHT = 1000, 500

# colors
WHITE = (255, 255, 255)

# boundaries and thresholds
UPPER_BOUNDARY = 10
BOTTOM_BOUNDARY = 450
FRAMES_TO_LOAD_PROJECTILE_THRESHOLD = 15 # it is linked with var frames_to_load_projectile in the Game class
DOUBLE_SHOOTING_FRAMES_THRESHOLD = 360 # the amount of frames that after them the Player's mode changes to single shooting

# factors
DIM_FACTOR = 0.8 # it decreases the base distance for collision detection method to make it more realistic and precisely
REPLICATE_FACTOR = 3 # it extends the lifetime of a single animation (positive int only)
FISH_CALLING_FREQUENCY_FACTOR = 1.0  # FCFF - it multiplies frequency of creating a single enemy (fish) on the screen
LUCKY_FISH_PERCENTAGE = 10 # probability of calling a Lucky fish type [%] (only int in range from 1 to 100 inclusive)

# background
BACKGROUND = load('assets/background.png') # 1768x500px

# seahorse
PLAYER = load('assets/player.png')
PLAYER_LIST = []
for i in range(4680//120):
    PLAYER_LIST.append(PLAYER.subsurface(i*120, 0, 120, 190))

PLAYER_2_LIST = []
for i in range(4680//120):
    PLAYER_2_LIST.append(PLAYER.subsurface(i*120, 190, 120, 190))
    
# enemies
ANGLER = load('assets/angler1.png')
ANGLER_LIST = []
for i in range(8892//228):
    ANGLER_LIST.append(ANGLER.subsurface(i*228, 0, 228, 169))

DRONE = load('assets/drone.png')
DRONE_LIST = []
for i in range(4485//115):
    DRONE_LIST.append(DRONE.subsurface(i*115, 0, 115, 95))

HIVEWHALE = load('assets/hivewhale.png')
HIVEWHALE_LIST = []
for i in range(15600//400):
    HIVEWHALE_LIST.append(HIVEWHALE.subsurface(i*400, 0, 400, 227))

LUCKY = load('assets/lucky.png')
LUCKY_LIST = []
for i in range(3861//99):
    LUCKY_LIST.append(LUCKY.subsurface(i*99, 0, 99, 95))

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

import pygame
from sh.constants import WIDTH, HEIGHT, FPS, FRAMES_TO_LOAD_PROJECTILE_THRESHOLD
from sh.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Seahorse by AW')

def main():
    clock = pygame.time.Clock()
    run = True
    game = Game(WIN)
    pygame.init() # it is needed for font module initialization

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)

            # projectile launching trigger
            if not game.gameover:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        if game.frames_to_load_projectile >= FRAMES_TO_LOAD_PROJECTILE_THRESHOLD:
                            game.player.launch_projectile()
                            game.frames_to_load_projectile = 0

        # player steering trigger
        if not game.gameover:
            keys = pygame.key.get_pressed() # zwraca slownik z wartosciami typu bool
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                game.player.move('up')
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                game.player.move('down')

        game.update()
        game.render()

    pygame.quit()

main()

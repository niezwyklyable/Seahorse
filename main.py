import pygame
from sh.constants import WIDTH, HEIGHT, FPS, FRAMES_TO_LOAD_PROJECTILE_THRESHOLD
from sh.game import Game
import pymunk
from pymunk import pygame_util

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Seahorse by AW')

def main():
    # pymunk stuff
    dt = 1/FPS
    space = pymunk.Space()
    space.gravity = (0, 981)
    draw_options = pygame_util.DrawOptions(WIN)

    # main settings
    clock = pygame.time.Clock()
    run = True
    pygame.init() # it is needed for font module initialization
    game = Game(WIN, space, draw_options)

    while run:
        clock.tick(FPS)
        space.step(dt)

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

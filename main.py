import pygame
from sh.constants import WIDTH, HEIGHT, FPS
from sh.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Seahorse by AW')

def main():
    clock = pygame.time.Clock()
    run = True
    game = Game(WIN)
    #pygame.init()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
    
        # player steering trigger
        keys = pygame.key.get_pressed() # zwraca slownik z wartosciami typu bool
        if keys[pygame.K_w]:
            game.player.move('up')
        elif keys[pygame.K_s]:
            game.player.move('down')

        game.update()
        game.render()

    pygame.quit()

main()

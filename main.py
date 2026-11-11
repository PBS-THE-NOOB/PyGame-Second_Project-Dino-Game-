import pygame
from Settings.constants import SCREEN_WIDTH,SCREEN_HEIGHT,FPS
from Game.world import World

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('DINO GAME')
clock = pygame.time.Clock()
world =  World(screen)

run = True
if __name__ == '__main__' : 

    while run:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                run = False
                
        world.draw()
        pygame.display.update()
        clock.tick(FPS)
        
    pygame.quit()

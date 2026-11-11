import pygame
from Settings.constants import SCREEN_WIDTH,SCREEN_HEIGHT,FPS
from Game.world import World
from Game.player import Player
from Game.Obsticals import Obsticals


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('DINO GAME')
clock = pygame.time.Clock()
# Game logic
world =  World(screen)
player = pygame.sprite.GroupSingle()
player.add(Player())
# obsticals = pygame.sprite.Group()
# obsticals.add(Obsticals('dead_tree'))

run = True
if __name__ == '__main__' : 

    while run:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                run = False

        world.draw()
        world.update()

        player.draw(screen)
        player.update()

        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()

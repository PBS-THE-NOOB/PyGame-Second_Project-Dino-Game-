import pygame,random
from Settings.constants import SCREEN_WIDTH,SCREEN_HEIGHT,FPS
from Game.world import World
from Game.player import Player
from Game.Obsticals import Obsticals
from Game.Game_fundamentals import Game_Play


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('DINO GAME')
clock = pygame.time.Clock()

# Game logic
world =  World(screen)
player = pygame.sprite.GroupSingle()
player.add(Player())
GAME_ACTIVE = True
game = Game_Play(screen)

#Obsticals logic
obsticals = pygame.sprite.Group()
OBSTICAL_APPEAR = pygame.USEREVENT + 1
pygame.time.set_timer(OBSTICAL_APPEAR,1500)

run = True
if __name__ == '__main__' : 

    while run:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                run = False
            elif event.type == OBSTICAL_APPEAR and GAME_ACTIVE:
                if random.randint(0,3) : 
                    obsticals.add(Obsticals('dead_tree',random.randint(SCREEN_WIDTH + 100,SCREEN_WIDTH + 600)))
                else : 
                    obsticals.add(Obsticals('bird',random.randint(SCREEN_WIDTH + 100,SCREEN_WIDTH + 600)))
        if GAME_ACTIVE : 
            world.draw()
            world.update()

            player.draw(screen)
            player.update()

            obsticals.draw(screen)
            obsticals.update()

            if pygame.sprite.spritecollide(player.sprite,obsticals,False) : 
                GAME_ACTIVE = False

        if not GAME_ACTIVE :
            GAME_ACTIVE = game.Game_Over(GAME_ACTIVE)
            player.sprite.reset()
            obsticals.empty()

        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()

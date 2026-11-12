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
GAME_ACTIVE = False
game = Game_Play(screen)

#Obsticals logic
obsticals = pygame.sprite.Group()
OBSTICAL_APPEAR = pygame.USEREVENT + 1
pygame.time.set_timer(OBSTICAL_APPEAR,1500)

Starting_Time = 0

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
            Time = pygame.time.get_ticks()
            world.draw()
            world.update()

            game.display_score(Time,Starting_Time)

            player.draw(screen)
            player.update()

            obsticals.draw(screen)
            obsticals.update()

            if pygame.sprite.spritecollide(player.sprite,obsticals,False) : 
                GAME_ACTIVE = False
                Starting_Time = pygame.time.get_ticks()

        if not GAME_ACTIVE :
            if game.Game_Over(GAME_ACTIVE):
                player.sprite.reset()
                obsticals.empty()
                GAME_ACTIVE = True

        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()

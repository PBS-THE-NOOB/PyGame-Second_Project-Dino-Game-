import pygame
from Settings.constants import FOREST_GREEN,SCREEN_HEIGHT,SCREEN_WIDTH,RED

class Game_Play():
    def __init__(self,screen):
        self.text_font = pygame.font.Font(None,50)
        self.screen = screen
        

    def Game_Over(self,GAMEACTIVE):
        if not GAMEACTIVE:
            self.screen.fill(FOREST_GREEN)
            text_surf = self.text_font.render('GAME OVER',0,RED)
            text_rect = text_surf.get_rect(center = (SCREEN_WIDTH//2,300))
            self.screen.blit(text_surf,text_rect)
            return self.check_enter()
        
    def check_enter(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] : return True
        

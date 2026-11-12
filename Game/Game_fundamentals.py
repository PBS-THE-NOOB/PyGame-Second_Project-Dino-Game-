import pygame
from Settings.constants import FOREST_GREEN,SCREEN_WIDTH,RED,BLUE,GREEN

class Game_Play():
    def __init__(self,screen):
        self.text_font = pygame.font.Font(None,50)
        self.screen = screen
        self.score = 0
        self.score_surf = self.text_font.render(f'Score : {self.score}',0,BLUE)
        self.score_rect = self.score_surf.get_rect(topleft = (0,0))

    def Game_Over(self,GAMEACTIVE):
        if not GAMEACTIVE:
            self.screen.fill(FOREST_GREEN)
            Game_Over_surf = self.text_font.render('GAME OVER',0,RED)
            Game_Over_rect = Game_Over_surf.get_rect(bottomleft = (SCREEN_WIDTH //3 + 75,300))
            Click_enter_surf = self.text_font.render('Click Enter to Continue',0,RED)
            Click_enter_rect = Click_enter_surf.get_rect(topleft = (SCREEN_WIDTH // 3,300))
            self.screen.blit(Game_Over_surf,Game_Over_rect)
            self.screen.blit(Click_enter_surf,Click_enter_rect)
            self.screen.blit(self.score_surf,self.score_rect)
            return self.check_enter()
        
    def check_enter(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] : return True

    def display_score(self,time,starting_time) :
        self.score = (time - starting_time) / 10
        self.score_surf = self.text_font.render(f'Score : {self.score}',0,BLUE)
        self.screen.blit(self.score_surf,(0 , 50))
        

import pygame
from Settings.constants import SCREEN_HEIGHT,SCREEN_WIDTH,GROUND_HEIGHT

class World():
    def __init__(self,screen):
        self.screen = screen
        self.background_sky = pygame.transform.scale(pygame.image.load('Background/sky.png').convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.ground = pygame.transform.scale(pygame.image.load('Background/ground.png').convert(),(SCREEN_WIDTH,GROUND_HEIGHT))
        self.ground_rect = self.ground.get_rect(bottomleft = (0,SCREEN_HEIGHT))
        
    def draw(self):
        self.screen.blit(self.background_sky,(0,0))
        self.screen.blit(self.ground,self.ground_rect)
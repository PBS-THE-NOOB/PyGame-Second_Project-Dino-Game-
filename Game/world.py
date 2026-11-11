import pygame
from Settings.constants import SCREEN_HEIGHT,SCREEN_WIDTH,GROUND_HEIGHT

class World():
    def __init__(self,screen):
        self.screen = screen
        self.background_sky = pygame.transform.scale(pygame.image.load('Background/sky.png').convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.ground = pygame.transform.scale(pygame.image.load('Background/ground.png').convert(),(SCREEN_WIDTH,GROUND_HEIGHT))
        self.ground_rect = self.ground.get_rect(bottomleft = (0,SCREEN_HEIGHT))
        self.ground_rect_2 = self.ground.get_rect(bottomleft = (SCREEN_WIDTH,SCREEN_HEIGHT))
        self.scrooling_val = 2

    def scrolling_ground(self):
        if self.ground_rect.left <= -self.ground_rect.width :
            self.ground_rect.left = SCREEN_WIDTH
        if self.ground_rect_2.left <= -self.ground_rect.width :
            self.ground_rect_2.left = SCREEN_WIDTH
        self.ground_rect.x -= int(self.scrooling_val)
        self.ground_rect_2.x -= int(self.scrooling_val)

    def draw(self):
        self.screen.blit(self.background_sky,(0,0))
        self.screen.blit(self.ground,self.ground_rect)
        self.screen.blit(self.ground,self.ground_rect_2)

    def update(self):
        self.scrolling_ground()
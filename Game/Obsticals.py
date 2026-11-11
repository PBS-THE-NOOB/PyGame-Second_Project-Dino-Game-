import pygame
from Settings.constants import DEAD_TREE_HEIGHT,DEAD_TREE_WIDTH,GROUND_Y_COORDINATE

class Obsticals(pygame.sprite.Sprite):

    def __int__(self,type):
        super().__init__()
        if type == 'dead_tree' : 
            self.image = pygame.transform.scale(pygame.image.load('sprites/tree_dead.png').convert_alpha(),(DEAD_TREE_WIDTH,DEAD_TREE_HEIGHT))
        self.rect = self.image.get_rect()

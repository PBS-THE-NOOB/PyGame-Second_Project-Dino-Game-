import pygame 
from Settings.constants import DEAD_TREE_HEIGHT,DEAD_TREE_WIDTH,GROUND_Y_COORDINATE

class Obsticals(pygame.sprite.Sprite):

    def __init__(self,type,x_coordinate : int):
        super().__init__()
        self.type = type
        if self.type == 'dead_tree' : 
            self.image = pygame.transform.scale(pygame.image.load('sprites/tree_dead.png').convert_alpha(),(DEAD_TREE_WIDTH,DEAD_TREE_HEIGHT))
            self.rect = self.image.get_rect(midbottom = (x_coordinate,GROUND_Y_COORDINATE))
        elif self.type == 'bird' :
            spritesheet = pygame.transform.flip(pygame.image.load('sprites/Bird_Fly.png').convert_alpha(),1,0)
            num_of_frames = 6
            frame_width = spritesheet.get_width() // num_of_frames
            frame_height = spritesheet.get_height()
            self.frame_list = [spritesheet.subsurface(i * frame_width,0,frame_width,frame_height) for i in range(num_of_frames)]
            self.index = 0
            self.image = self.frame_list[self.index]
            self.rect = self.image.get_rect(midbottom = (x_coordinate,GROUND_Y_COORDINATE - 100))

    def animate_bird(self):
        if self.type == 'bird': 
            self.index += 0.2
            if self.index >= len(self.frame_list): self.index = 0
            self.image = self.frame_list[int(self.index)]

    def move_obsticals(self):
        if self.type == 'bird' : 
            self.rect.x -= 5
        else : self.rect.x -= 5
        if self.rect.right <= -50 : self.kill()

    def update(self):
        self.animate_bird()
        self.move_obsticals()
        
        

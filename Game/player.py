import pygame
from Settings.constants import PLAYER_HEIGHT,PLAYER_WIDTH,GROUND_Y_COORDINATE,PLAYER_BOTTOM_OFFSET

PLAYER_GROUND_Y = GROUND_Y_COORDINATE + PLAYER_BOTTOM_OFFSET

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_frames = [pygame.transform.scale(pygame.image.load(f'sprites/Spino/Spino_Walk_{i:02d}.png').convert_alpha(),(PLAYER_WIDTH,PLAYER_HEIGHT)) for i in range (1,12)]
        self.player_index = 0
        self.image = self.image_frames[int(self.player_index)]
        self.rect = self.image.get_rect(midbottom = (100,PLAYER_GROUND_Y))
        self.grounded = True
        self.gravity = 0

    def animate_player(self):
        if self.rect.bottom == PLAYER_GROUND_Y :
            self.player_index += 0.2
            if self.player_index >= len(self.image_frames) : self.player_index = 0
            self.image = self.image_frames[int(self.player_index)] 

    def apply_gravity(self):

        keys = pygame.key.get_pressed()
        if self.rect.bottom == PLAYER_GROUND_Y and keys[pygame.K_SPACE] :
            self.gravity = -20 
            self.grounded = False

        if not self.grounded :
            self.gravity += 1
            self.rect.y += self.gravity
            self.grounded = False

        if self.rect.bottom > PLAYER_GROUND_Y : 
            self.rect.bottom = PLAYER_GROUND_Y 
            self.gravity = 0
            self.grounded = True

    def update(self):
        self.apply_gravity()
        self.animate_player()
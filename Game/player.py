import pygame
from Settings.constants import PLAYER_HEIGHT,PLAYER_WIDTH

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_list = [pygame.transform.scale(pygame.image.load(f'sprites/Spino/Spino_Walk_{i:02d}.png').convert_alpha(),(PLAYER_WIDTH,PLAYER_HEIGHT)) for i in range (1,12)]
        self.player_index = 0
        self.player_surf = self.player_list[int(self.player_index)]
        self.player_rect = self.player_surf.get_rect()

    def animate_player(self):
        self.player_index += 0.2
        if self.player_index >= len(self.player_list) : self.player_index = 0
        player_surf = self.player_list[int(self.player_index)]
        return player_surf 
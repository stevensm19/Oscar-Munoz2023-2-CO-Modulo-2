import pygame
from pygame.sprite import Sprite
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE, DEFAULT_TYPE,SCREEN_WIDTH,SCREEN_HEIGHT

class Hammer(Sprite):

    def __init__(self):
        self.image = HAMMER  
        self.hammer_rect = self.image.get_rect()
        self.hammer_rect.x = 80
        self.hammer_rect.y = 310
        self.index = 0
    
    def draw(self, screen):
        screen.blit(self.image, self.hammer_rect)

    def update(self,game):
        self.hammer_rect.x += 20
        if self.hammer_rect.x > SCREEN_WIDTH:
           game.test_hammer = False
           self.hammer_rect.x = 80
import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH
class Menu:
    half_screen_width = SCREEN_WIDTH
    half_screen_height = SCREEN_HEIGHT
    def __init__(self,screen,message):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE,30)
        self.text = self.font.render(message, True, (0,0,0))
        self.text.rect = self.text.get_rect()
        self.text.x = self.half_screen_width
        self.text.y = self.half_screen_height

    def update (self):
        pass
    def draw (self):
        pass
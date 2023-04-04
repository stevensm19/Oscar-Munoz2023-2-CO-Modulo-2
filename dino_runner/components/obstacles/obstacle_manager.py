import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = [] #bird, small, large
    
    def update (self,game):
        if len(self.obstacles) == 0:
            small_cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(small_cactus)
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw (self,screen):
        
        for obstacle in self.obstacles:
            obstacle.draw(screen)
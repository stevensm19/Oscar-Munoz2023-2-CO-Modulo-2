import pygame
import random
from dino_runner.components.obstacles.small_cactus import smallCactus
from dino_runner.components.obstacles.large_cactus import largeCactus
from dino_runner.components.obstacles.bird import bird

from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = [] #bird o small o large

    def update (self,game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(smallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(largeCactus(LARGE_CACTUS))    
            elif random.randint(0, 2) == 2:
                self.obstacles.append(bird(BIRD))        
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw (self,screen):
        
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def fly (self): #Metodo para agacharse
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 1
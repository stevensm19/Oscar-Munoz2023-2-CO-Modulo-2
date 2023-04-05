import pygame
import random
from dino_runner.components.dinosaur import Dinosour
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = [] #bird o small o large

    def update (self,game):
        #agregar obstacule_type
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacles(random.randint(0, 2))
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                game.death_count += 1
                break

    def draw (self,screen):
        
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def generate_obstacles(self,obstacle_type):
        if obstacle_type == 0:
            cactus_type = "SMALL"
            obstacle = Cactus(cactus_type)
        elif obstacle_type == 1:
            cactus_type = "LARGE"
            obstacle = Cactus(cactus_type)
        else:
            obstacle = Bird()    
        return obstacle

    def reset_obstacles(self):
        self.obstacles = []    
import random
import pygame
from dino_runner.components import obstacles
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.components.power_ups.hammer import Hammer


from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, DEFAULT_TYPE, HAMMER

class ObstacleManager:

    def __init__(self):

        self.obstacles = []
        self.hammer = Hammer()

    def update(self, game):

        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle(random.randint(0, 2))
            self.obstacles.append(obstacle)

        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE and game.player.type != HAMMER_TYPE:
                    game.playing = False
                    game.death_count.update()
                    game.player.type = DEFAULT_TYPE
                    break
                else:
                    self.obstacles.remove(obstacle)
            
            

    def draw(self, screen):

        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def generate_obstacle(self, obstacle_type):

        if obstacle_type == 0:
            cactus_type = 'SMALL'
            obstacle = Cactus(cactus_type)
        elif obstacle_type == 1:
            cactus_type = 'LARGE'
            obstacle = Cactus(cactus_type)
        else:
            obstacle = Bird()
        return obstacle

    def reset_obstacles(self):
        self.obstacles = []

import random

from dino_runner.components.obstacles.obstacle import Obstacle 
from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.utils.constants import BIRD

class Bird(Obstacle): 
    BIRD_HEIGHTS = [260,220,170]

    def __init__ (self):
        self.type = 0
        super().__init__(BIRD,self.type)
        self.rect.y = self.BIRD_HEIGHTS[random.randint(0, 2)]
        self.fly_index = 0

    def draw(self, screen):
        if self.fly_index >= 10:
            self.fly_index = 0
        self.image = BIRD[0] if self.fly_index < 5 else BIRD[1]
        
        screen.blit(self.image, self.rect)
        self.fly_index += 1
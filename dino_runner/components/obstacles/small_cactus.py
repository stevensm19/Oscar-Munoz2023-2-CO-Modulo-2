import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH 

class smallCactus(Obstacle):
    def __init__ (self,image):
        self.image = image
        self.type = random.randint(0, 2)
        super().__init__(self.image,self.type)
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 325
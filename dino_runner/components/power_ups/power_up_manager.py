import pygame
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, DEFAULT_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3,5)
        self.when_appears = random.randint(50,70)

    def update(self,game):
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            power_up = self.generate_power_up(random.randint(0, 1))

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)    
            if game.player.dino_rect.colliderect(power_up.rect):
                self.power_ups.remove(power_up)
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = self.type
                game.player.power_up_time = power_up.start_time + (self.duration * 1000)
                

    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []            
        self.when_appears = random.randint(50,70)

    def generate_power_up(self, power_up_type):
        if power_up_type == 0:
            self.when_appears += random.randint(150, 200)
            power_up = Shield()        
            self.type = SHIELD_TYPE
        else:
            self.when_appears += random.randint(50, 100)
            power_up = Hammer()        
            self.type = HAMMER_TYPE

        self.power_ups.append(power_up)
        
        
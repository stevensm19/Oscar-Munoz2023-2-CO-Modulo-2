import pygame
import random

from dino_runner.components.power_ups.power_shield import PowerShield
from dino_runner.components.power_ups.power_hammer import PowerHammer
from dino_runner.components.power_ups.hammer import Hammer


from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, DEFAULT_TYPE, HAMMER

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.hammer = Hammer()
        self.duration = random.randint(3,5)
        self.when_appears = random.randint(50,70)

    def update(self,game):
        user_input = pygame.key.get_pressed()
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            # power_up = self.generate_power_up(random.randint(0, 1))
            power_up = self.generate_power_up(1)

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)    
            if game.player.dino_rect.colliderect(power_up.rect):
                self.power_ups.remove(power_up)
                game.test_hammer = False
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = self.type
                game.player.power_up_time = power_up.start_time + (self.duration * 1000)
        #Homework - 4 
        if game.player.type == HAMMER_TYPE and user_input[pygame.K_SPACE] and game.player.dino_run:
            game.player.type = DEFAULT_TYPE
            game.test_hammer = True
        #<-------    

    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []            
        self.when_appears = random.randint(50,70)

    def generate_power_up(self, power_up_type):
        if power_up_type == 0:
            self.when_appears += random.randint(100, 150)
            power_up = PowerShield()        
            self.type = SHIELD_TYPE
        #Homework - 4    
        else:
            self.when_appears += random.randint(50, 100)
            power_up = PowerHammer()    
            self.type = HAMMER_TYPE
        #<-------    

        self.power_ups.append(power_up)
        
        
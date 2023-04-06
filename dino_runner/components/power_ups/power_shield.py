from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE, HAMMER, HAMMER_TYPE

class PowerShield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)
        self.rect.y = 125
  
        

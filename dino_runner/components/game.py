import pygame
import random
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE, DEAD
from dino_runner.components.menu import Menu
from dino_runner.components.dinosaur import Dinosour
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager


class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        pygame.display.set_icon(DEAD)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = SCREEN_WIDTH #nube
        self.y_pos_cloud = random.randint(10,50) #nube
        self.player = Dinosour()
        self.obstacle_manager = ObstacleManager()
        self.running = False
        self.score = 0
        self.death_count = 0
        self.max_score = 0
        self.menu = Menu(self.screen, "Press any key to start...")

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.game_speed = self.GAME_SPEED
        self.score = 0
        while self.playing:
            self.events()
            self.update() 
            self.draw() 
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
   
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        self.update_score()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255,255,255))
        self.draw_background()
        self.draw_cloud()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()
        

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed 

    def draw_cloud(self): #nube
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
        
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = SCREEN_WIDTH + random.randint(0,20)
        self.x_pos_cloud -= self.game_speed     

    def show_menu(self): #aca se coloca cantidad de muertes y score actual y maximo
        self.menu.reset_screen_color(self.screen)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        self.screen.blit(DEAD, (half_screen_width - 50, half_screen_height -140))
        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            self.menu.update_message(f'Dino has died {self.death_count} times :(')
            self.menu.draw(self.screen)    
        self.menu.update(self)

    def update_score(self):
        self.score += 0.1
        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5
        print(self.score)


    def draw_score(self):

        if self.score > self.max_score:
            self.max_score = self.score

        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"Max Score: {int(self.max_score)}", True, (0, 0, 0))
        score = font.render(f"Score: {int(self.score)}", True, (0, 0, 0))


        text_rect = text.get_rect()
        text_rect.center = (965, 50)

        score_rect = score.get_rect()
        score_rect.center = (1000, 80)

        self.screen.blit(text, text_rect)

        self.screen.blit(score, score_rect)
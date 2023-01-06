import pygame
from game import Game
class HomeScreen(object):
    def __init__(self, height, width, player_size, player_speed, start_ammo, bullet_size, enemy_size,
    bullet_speed) -> None:
        self.height = height
        self.width = width
        self.window = pygame.display.set_mode((self.height, self.width))
        self.player_size = player_size
        self.player_speed = player_speed
        self.start_ammo = start_ammo
        self.bullet_size = bullet_size
        self.enemy_size = enemy_size
        self.bullet_speed = bullet_speed
    def set_window_background(self):
        background_img = pygame.image.load('assets/background.png').convert_alpha()
        background_img = pygame.transform.scale(background_img, (self.height, self.width))
        self.window.blit(background_img, (0,0))
    def display_text(self):
        font = pygame.font.Font('assets/Roboto-Black.ttf', 72)
        text_title = font.render(f'Budget Space Invader', True, (17,255,0), (3,12,16))
        text_rect = text_title.get_rect()
        text_rect.center = (self.height//2, self.width//2-150)
        self.window.blit(text_title, text_rect)
        font2 = pygame.font.Font('assets/Roboto-Black.ttf', 26)
        text_sub = font2.render(f'A fun little project inspired by the upcoming finals :)', True, (17,255,0), (3,12,16))
        text_rect_2 = text_sub.get_rect()
        text_rect_2.center = (self.height//2, self.width//2-95)
        self.window.blit(text_sub, text_rect_2)
    def display_play_button(self, param='red'):
        font = pygame.font.Font('assets/Roboto-Black.ttf', 72)
        if param == 'green':
            text_title = font.render(f'Play', True, (0,255,0), (3,12,16))
        else:
            text_title = font.render(f'Play', True, (255,0,0), (3,12,16))
        text_rect = text_title.get_rect()
        text_rect.center = (self.height//2-100, self.width//2)
        self.play_button = text_rect
        self.window.blit(text_title, text_rect)
    def display_quit_button(self, param='red'):
        font2 = pygame.font.Font('assets/Roboto-Black.ttf', 72)
        if param == 'green':
            text_title2 = font2.render(f'Quit', True, (0,255,0), (3,12,16))
        else:
            text_title2 = font2.render(f'Quit', True, (255,0,0), (3,12,16))
        text_rect2 = text_title2.get_rect()
        text_rect2.center = (self.height//2+100, self.width//2)
        self.quit_button = text_rect2
        self.window.blit(text_title2, text_rect2)
    def handle_hover(self):
        if self.play_button.collidepoint(pygame.mouse.get_pos()):
            self.display_play_button('green')
        else:
            self.display_play_button()
        if self.quit_button.collidepoint(pygame.mouse.get_pos()):
            self.display_quit_button('green')
        else:
            self.display_quit_button()
    def handle_click_play(self):
        click = pygame.mouse.get_pressed(3)[0] and self.play_button.collidepoint(pygame.mouse.get_pos())
        if click:
            self.window = None
            Game(self.height, self.width, self.player_size, self.player_speed, self.start_ammo, 
            self.bullet_size, self.enemy_size,self.bullet_speed).run()
    def handle_click_quit(self):
        click = pygame.mouse.get_pressed(3)[0] and self.quit_button.collidepoint(pygame.mouse.get_pos())
        if click:
            pygame.quit()
        
    def run(self):
        pygame.init()
        pygame.display.set_caption('Budget Space Invader')
        self.set_window_background()
        self.display_text()
        self.display_play_button()
        self.display_quit_button()
        while True:
            self.handle_hover()
            self.handle_click_play()
            self.handle_click_quit()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            pygame.display.update()
if __name__ == "__main__":
    print('Not meant to start like that')
    pass
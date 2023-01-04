import pygame
from player import Player
class Game():
    def __init__(self, height, width, player_size, player_speed, start_ammo, bullet_size, enemy_size,
    bullet_speed) -> None:
        self.WINDOW_HEIGHT = height
        self.WINDOW_WIDTH = width
        self.window = pygame.display.set_mode((self.WINDOW_HEIGHT, self.WINDOW_WIDTH))
        self.enemis_hitboxes = []
        self.player = Player(player_size, player_size, 590, 550)
        self.player_speed= player_speed
        self.ammo = start_ammo
        self.lastTimeShot = 0
        self.bullet_hitboxes = []
        self.bullet_size = bullet_size
        self.enemy_size = enemy_size
        self.bullet_velocity = bullet_speed
        self.player_size = player_size
    def spawn_player(self,hitbox: pygame.Rect):
        player_img = pygame.image.load('assets/spaceship.png').convert_alpha()
        player_img = pygame.transform.scale(player_img, (self.player_size, self.player_size))
        self.window.blit(player_img, (hitbox.x,hitbox.y))
    def set_window_background(self):
        background_img = pygame.image.load('assets/background.png').convert_alpha()
        background_img = pygame.transform.scale(background_img, (self.WINDOW_HEIGHT, self.WINDOW_WIDTH))
        self.window.blit(background_img, (0,0))
    def generate_enemy_pos_list(self):
        for i in range(3):
            self.enemis_hitboxes.append([])
            for j in range(10):
                self.enemis_hitboxes[i].append(None)
    def handle_player_movement(self,keys_pressed, player_hitbox):
    
        # if keys_pressed[pygame.K_w]:
        #     hitbox.y -= BASE_MOVEMENT
        # if keys_pressed[pygame.K_s]:
        #     hitbox.y += BASE_MOVEMENT
        if keys_pressed[pygame.K_a]:
            if player_hitbox.x < 10:
                return
            player_hitbox.x -= self.player_speed
        if keys_pressed[pygame.K_d]:
            if player_hitbox.x > 1180:
                return
            player_hitbox.x += self.player_speed
        if keys_pressed[pygame.K_SPACE]:
            self.shoot(player_hitbox)
    def shoot(self, hitbox: pygame.Rect):
        if self.ammo <= 0 or pygame.time.get_ticks() - self.lastTimeShot < 500:
            return
        self.lastTimeShot = pygame.time.get_ticks()
        self.ammo-=1
        self.bullet_hitboxes.append(pygame.Rect(hitbox.x+40,hitbox.y, self.bullet_size // 2, self.bullet_size))
    def spawn_enemies(self,num_of_enemies_to_spawn):
        for i in range(len(self.enemis_hitboxes)):
            for j in range(len(self.enemis_hitboxes[i])):
                if num_of_enemies_to_spawn <= 0:
                    return
                if self.enemis_hitboxes[i][j] == None:
                    self.enemis_hitboxes[i][j] = pygame.Rect(50+j*(self.enemy_size+20), i*(self.enemy_size+20), self.enemy_size, self.enemy_size)
                    num_of_enemies_to_spawn-=1
    def detect_collisions(self):
        for bullet in self.bullet_hitboxes:
            for i in range(len(self.enemis_hitboxes)):
                for j in range(len(self.enemis_hitboxes[i])):
                    if self.enemis_hitboxes[i][j] == None:
                        return
                    if bullet.colliderect(self.enemis_hitboxes[i][j]):

                        self.enemis_hitboxes[i].remove(self.enemis_hitboxes[i][j])
                        self.bullet_hitboxes.remove(bullet)
                        return          
    def draw_enemies(self):
        enemy_image = pygame.image.load('assets/enemy.png').convert_alpha()
        enemy_image = pygame.transform.scale(enemy_image, (self.enemy_size, self.enemy_size))
        for i in range(len(self.enemis_hitboxes)):
            for j in range(len(self.enemis_hitboxes[i])):
                enemy = self.enemis_hitboxes[i][j]
                if enemy == None:
                    return
                self.window.blit(enemy_image, (enemy.x,enemy.y))
    def animatebullets(self):
        bullet_image = pygame.image.load('assets/bullet.png').convert_alpha()
        bullet_image = pygame.transform.scale(bullet_image, (self.bullet_size // 2, self.bullet_size))
        for bullet in self.bullet_hitboxes:
            self.window.blit(bullet_image, (bullet.x,bullet.y))
    def movebullets_and_delete_when_out_of_screen(self):##TOFIX
        for bullet in range(len(self.bullet_hitboxes)):
                self.bullet_hitboxes[bullet].y-=self.bullet_velocity
                if self.bullet_hitboxes[bullet].y < -50:
                    del self.bullet_hitboxes[bullet]
                    break
    def run(self):
        pygame.init()
        pygame.display.set_caption('Budget Space Invader')
        currentWaveOfEnemies = 15
        self.set_window_background()
        player_hitbox = pygame.Rect(590,550 , 100, 100)
        pygame.time.Clock().tick(60)
        notSpawned = True
        self.generate_enemy_pos_list()
        while True:
            self.set_window_background()
            self.spawn_player(player_hitbox)
            
            if notSpawned:
                self.spawn_enemies(currentWaveOfEnemies)
                notSpawned = False
            self.draw_enemies()
            self.handle_player_movement(pygame.key.get_pressed(), player_hitbox)
            self.animatebullets()
            self.movebullets_and_delete_when_out_of_screen()
            self.detect_collisions()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    return
            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    print('Not meant to start like that')
    pass
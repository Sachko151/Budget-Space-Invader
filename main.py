import pygame, random
pygame.init()
WINDOW_HEIGHT, WINDOW_WIDTH = 1280, 720
BULLET_SIZE = 40
ENEMY_SIZE = 100
BULLET_VELOCITY = 20
player_ammo = 10
lastTimeShot = 0
BASE_MOVEMENT = 5

window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
bullet_hitboxes = []
enemis_hitboxes = []
pygame.display.set_caption('Budget Space Invader')
def set_window_background():
    background_img = pygame.image.load('assets/background.png')
    background_img = pygame.transform.scale(background_img, (WINDOW_HEIGHT, WINDOW_WIDTH))
    window.blit(background_img, (0,0))
def spawn_player(hitbox: pygame.Rect):
    player_img = pygame.image.load('assets/spaceship.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (100, 100))
    window.blit(player_img, (hitbox.x,hitbox.y))
def handle_player_movement(keys_pressed, hitbox):
    
    if keys_pressed[pygame.K_w]:
        hitbox.y -= BASE_MOVEMENT
    if keys_pressed[pygame.K_s]:
        hitbox.y += BASE_MOVEMENT
    if keys_pressed[pygame.K_a]:
        hitbox.x -= BASE_MOVEMENT
    if keys_pressed[pygame.K_d]:
        hitbox.x += BASE_MOVEMENT
    if keys_pressed[pygame.K_SPACE]:
        shoot(hitbox)
def shoot(hitbox: pygame.Rect):
    global player_ammo
    global lastTimeShot
    if player_ammo <= 0 or pygame.time.get_ticks() - lastTimeShot < 500:
        return
    lastTimeShot = pygame.time.get_ticks()
    player_ammo-=1
    bullet_hitboxes.append(pygame.Rect(hitbox.x,hitbox.y, BULLET_SIZE // 2, BULLET_SIZE))
def spawn_enemies(num_of_enemies):
    # rand_X = random.randint(10,1200)
    # rand_Y = random.randint(10, 270)
    for x in range(num_of_enemies - len(enemis_hitboxes)):
        if x == 0:
            enemis_hitboxes.append(pygame.Rect(0, 0 , ENEMY_SIZE, ENEMY_SIZE))
            continue
        last_pos_x = enemis_hitboxes[-1].x
        last_pos_y = enemis_hitboxes[-1].y
        rand_offset_x = random.randint(ENEMY_SIZE, ENEMY_SIZE * 2)
        rand_offset_y = random.randint(0, ENEMY_SIZE)
        enemis_hitboxes.append(pygame.Rect(last_pos_x+rand_offset_x, last_pos_y+rand_offset_y , ENEMY_SIZE, ENEMY_SIZE))
    


               
        
def draw_enemies():
    enemy_image = pygame.image.load('assets/enemy.png').convert_alpha()
    enemy_image = pygame.transform.scale(enemy_image, (ENEMY_SIZE, ENEMY_SIZE))
    for enemy in enemis_hitboxes:
        window.blit(enemy_image, (enemy.x,enemy.y))

def animatebullets():
    bullet_image = pygame.image.load('assets/bullet.png').convert_alpha()
    bullet_image = pygame.transform.scale(bullet_image, (BULLET_SIZE // 2, BULLET_SIZE))
    for bullet in bullet_hitboxes:
        window.blit(bullet_image, (bullet.x,bullet.y))
def movebullets_and_delete_when_out_of_screen():##TOFIX
    for bullet in range(len(bullet_hitboxes)):
        bullet_hitboxes[bullet].y-=BULLET_VELOCITY
        if bullet_hitboxes[bullet].y < -50:
           del bullet_hitboxes[bullet]
           break
def main():
    enemies = 5
    set_window_background()
    player_hitbox = pygame.Rect(0,0 , 100, 100)
    pygame.time.Clock().tick(60)
    while True:
        
        set_window_background()
        spawn_enemies(enemies)
        draw_enemies()
        spawn_player(player_hitbox)
        handle_player_movement(pygame.key.get_pressed(), player_hitbox)
        animatebullets()
        movebullets_and_delete_when_out_of_screen()
        #print(bullet_hitboxes)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
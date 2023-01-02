import pygame, random
pygame.init()
WINDOW_HEIGHT, WINDOW_WIDTH = 1280, 720
BULLET_SIZE = 40
ENEMY_SIZE = 100
BULLET_VELOCITY = 20
player_ammo = 101
lastTimeShot = 0
BASE_MOVEMENT = 15
PLAYER_SIZE = 100

window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
bullet_hitboxes = []
enemis_hitboxes = []
pygame.display.set_caption('Budget Space Invader')
def generate_enemy_pos_list():
    for i in range(3):
        enemis_hitboxes.append([])
        for j in range(10):
            enemis_hitboxes[i].append(None)
def set_window_background():
    background_img = pygame.image.load('assets/background.png').convert_alpha()
    background_img = pygame.transform.scale(background_img, (WINDOW_HEIGHT, WINDOW_WIDTH))
    window.blit(background_img, (0,0))
def spawn_player(hitbox: pygame.Rect):
    player_img = pygame.image.load('assets/spaceship.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (PLAYER_SIZE, PLAYER_SIZE))
    window.blit(player_img, (hitbox.x,hitbox.y))
def handle_player_movement(keys_pressed, hitbox):
    
    # if keys_pressed[pygame.K_w]:
    #     hitbox.y -= BASE_MOVEMENT
    # if keys_pressed[pygame.K_s]:
    #     hitbox.y += BASE_MOVEMENT
    if keys_pressed[pygame.K_a]:
        if hitbox.x < 10:
            return
        hitbox.x -= BASE_MOVEMENT
    if keys_pressed[pygame.K_d]:
        if hitbox.x > 1180:
            return
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
    bullet_hitboxes.append(pygame.Rect(hitbox.x+40,hitbox.y, BULLET_SIZE // 2, BULLET_SIZE))
def spawn_enemies(num_of_enemies_to_spawn):
    for i in range(len(enemis_hitboxes)):
        for j in range(len(enemis_hitboxes[i])):
            if num_of_enemies_to_spawn <= 0:
                return
            if enemis_hitboxes[i][j] == None:
                enemis_hitboxes[i][j] = pygame.Rect(50+j*(ENEMY_SIZE+20), i*(ENEMY_SIZE+20), ENEMY_SIZE, ENEMY_SIZE)
                num_of_enemies_to_spawn-=1
def detect_collisions():
    for bullet in bullet_hitboxes:
        for i in range(len(enemis_hitboxes)):
            for j in range(len(enemis_hitboxes[i])):
                if enemis_hitboxes[i][j] == None:
                    return
                if bullet.colliderect(enemis_hitboxes[i][j]):

                    enemis_hitboxes[i].remove(enemis_hitboxes[i][j])
                    bullet_hitboxes.remove(bullet)
                    return          
        
def draw_enemies():
    enemy_image = pygame.image.load('assets/enemy.png').convert_alpha()
    enemy_image = pygame.transform.scale(enemy_image, (ENEMY_SIZE, ENEMY_SIZE))
    for i in range(len(enemis_hitboxes)):
        for j in range(len(enemis_hitboxes[i])):
            enemy = enemis_hitboxes[i][j]
            if enemy == None:
                return
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
    currentWaveOfEnemies = 15
    set_window_background()
    player_hitbox = pygame.Rect(590,550 , 100, 100)
    pygame.time.Clock().tick(60)
    notSpawned = True
    generate_enemy_pos_list()
    while True:
        set_window_background()
        spawn_player(player_hitbox)
        
        if notSpawned:
            spawn_enemies(currentWaveOfEnemies)
            notSpawned = False
        draw_enemies()
        handle_player_movement(pygame.key.get_pressed(), player_hitbox)
        animatebullets()
        movebullets_and_delete_when_out_of_screen()
        detect_collisions()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
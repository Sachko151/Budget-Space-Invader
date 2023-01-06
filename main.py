from game import Game
from home_screen import HomeScreen
class Main():
    def __init__(self, height, width, player_size, player_speed, start_ammo, bullet_size, enemy_size,
    bullet_speed) -> None:
        self.game = HomeScreen(height, width, player_size, player_speed, start_ammo, bullet_size, enemy_size,
    bullet_speed)

    def start(self):
        self.game.run()
   

if __name__ == "__main__":
    WINDOW_HEIGHT, WINDOW_WIDTH = 1280, 720
    BULLET_SIZE = 40
    ENEMY_SIZE = 100
    BULLET_VELOCITY = 20
    player_ammo = 10
    BASE_MOVEMENT = 15
    PLAYER_SIZE = 100
    main = Main(WINDOW_HEIGHT, WINDOW_WIDTH, PLAYER_SIZE, BASE_MOVEMENT, player_ammo, BULLET_SIZE, ENEMY_SIZE, BULLET_VELOCITY)
    main.start()
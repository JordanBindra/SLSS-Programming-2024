# pygame-exercise-jewelthief.py

# A Jewel Thief Clone

import random

import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)

NUM_COINS = 50
NUM_ENEMIES = 5



class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.images = [ 
            pg.image.load("./Images/mario_360.png"), 
            pg.transform.flip(pg.image.load("./Images/mario_360.png"), True, False),
        ]

        self.facing = 0  # 0 is right
        self.image = self.images[self.facing]

        self.rect = self.image.get_rect()

    def update(self):
        """Update the location of Mario with the mouse"""
        next_pos = pg.mouse.get_pos()

        if self.rect.centerx > next_pos[0]:
            self.facing = 1
        elif self.rect.centerx < next_pos[0]:
            self.facing = 0

        self.image = self.images[self.facing]

        self.rect.center = next_pos

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/coin_360.png")
        self.rect = self.image.get_rect()

        # Randomize initial location
       
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

class Snail (pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/Snail.webp")

        self.image = pg.transform.scale(
            self.image,
            (self.image.get_width() // 10, self.image.get_height() // 10)
        )

        self.rect = self.image.get_rect()

       # Randomize initial location
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

        self.vel_x = random.choice([-6, -5, -4, 4, 5, 6])
        self.vel_y = random.choice([-6, -5, -4, 4, 5, 6])

    def update(self):
            """Make the snail move and bounce"""
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y

            # Bounce off the edge of the screen
            if self.rect.top < 0:
                self.rect.top = 0  # keep it inside the screen
                self.vel_y *= -1
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
                self.vel_y *= -1
            if self.rect.left < 0:
                self.rect.left = 0
                self.vel_x *= -1
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
                self.vel_x *= -1


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # Hide the mouse
    pg.mouse.set_visible(False)

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    score = 0

    font = pg.font.SysFont("Impact", 24)

    # Sprite Groups
    all_sprites = pg.sprite.Group()
    coin_sprites = pg.sprite.Group()
    enemies_sprites = pg.sprite.Group()

    # Create Player object
    player = Player()
    all_sprites.add(player)

    # Create Coin objects
    for _ in range(NUM_COINS):
        coin = Coin()

        all_sprites.add(coin)
        coin_sprites.add(coin)

    # Create Emeny object 
    for _ in range(NUM_ENEMIES):
        enemy = Snail()

        all_sprites.add(enemy)
        enemies_sprites.add(enemy)

    pg.display.set_caption("Jewel Thief Clone (Nintendo Don't Sue Us)")

    # --Main Loop--
    collison_count = 0 
    while not done: 
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        all_sprites.update()

        # Get a list of ALL COINS Mario has collided with
        coins_collided = pg.sprite.spritecollide(player, coin_sprites, True)
        for coin in coins_collided:
           # Increase the score by 10 
           score += 10 

           print(f"Score: {score}")

        # If the coin_sprites group is empty, respawn all coins
        if len(coin_sprites) <= 0:
            for _ in range(NUM_COINS):
                coin = Coin()

                all_sprites.add(coin)
                coin_sprites.add(coin)

        # Check for collison between Mario and Snail 
        enemies_collided = pg.sprite.spritecollide(player, enemies_sprites, False)
        for enemy in enemies_collided: 
            collison_count += 1
            if collison_count >= 500: 
                print("GAME OVER")
                done = True 


        # --- Draw items
        screen.fill(WHITE)

        # Render score and lives 
        score_image = font.render(f"Score: {score}", True, BLACK) 
        lives_image = font.render(f"Lives: {int(500 - collison_count)}", True, RED)

        all_sprites.draw(screen) 

        # "Blit" the surface on the screen 
        screen.blit(score_image, (5, 5))
        screen.blit(lives_image, (5, 35))


        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()
# pygame-example-shmup.py
# Shoot 'em Up

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

WIDTH = 720
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/galaga.png")

        # Scale the image down
        self.image = pg.transform.scale(
            self.image, (self.image.get_width() // 2, self.image.get_height() // 2)
        )

        self.rect = self.image.get_rect()

    def update(self):
        """Follow the mouse."""
        self.rect.center = pg.mouse.get_pos()

        # Keep at bottom of screen
        if self.rect.top < HEIGHT - 200:
            self.rect.top = HEIGHT - 200


# TODO: Bullet class
#   - image of the bullets, picture? pygame rectangle?
#   - spawn at the player
#   - vertical movement
class Bullet(pg.sprite.Sprite):
    def __init__(self, player_loc: list):
        """
        Params:
            player_loc: xy coordinates of centerx and top of player
        """
        super().__init__()

        self.image = pg.Surface((10, 25))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

        # Set its initial position to player's centerx and top
        self.rect.centerx = player_loc[0]
        self.rect.bottom = player_loc[1]

        # Set the bullet velocity 
        self.vel = - 5 

    def update(self):
        """ Move the bullet up."""
        self.rect.y += self.vel

        # Remove the bullets if it goes of the screen
        # bottom of the bullet is negative
        if self.rect.bottom < 0:
            self.kill()
        

# TODO: Enemy class
#   - side to side movement
#   - keep it inside the screen

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/mario.png")

         # Scale the image down
        self.image = pg.transform.scale(
            self.image, (self.image.get_width() // 2, self.image.get_height() // 2)
        ) 

        self.rect = self.image.get_rect()

      # Set initial position randomly along the top of the screen
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, 150)  # Spawn enemies at the top portion of the screen

        # Set enemy horizontal velocity
        self.vel_x = random.choice([-3, 3]) 

        def update(self):
          """Move the enemy side to side"""
          self.rect.x += self.vel_x

        # Bounce off the sides of the screen
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.vel_x = -self.vel_x

def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    enemies = pg.sprite.Group()

    player = Player()

    all_sprites.add(player)

    pg.display.set_caption("Shoot 'Em Up")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # Create a new bullet
                all_sprites.add(Bullet((player.rect.centerx, player.rect.top)))

        # --- Update the world state
        all_sprites.update()

        print(len(all_sprites))

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps

    pg.quit()


def main():
    start()


if __name__ == "__main__":
    main()
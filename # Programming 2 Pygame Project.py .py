# Programming 2 Pygame Project.py 

# SNAKE 

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

WIDTH = 1500  # Pixels 
HEIGHT = 1200

SCREEN_SIZE = (WIDTH, HEIGHT) 

NUM_Food = 50
NUM_Hawk = 3

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/Snake.png")
        self.image = pg.transform.scale(
            self.image,
            (self.image.get_width() // 4, self.image.get_height() // 4)
        )
        self.rect = self.image.get_rect()

    def update(self):
        """Update the location of snake with the mouse"""
        next_pos = pg.mouse.get_pos()
        self.rect.center = next_pos
        print(self.rect.center)
    
    def grow(self):
        """Grow the snake by 5%"""
        
        # Scale the image up
        if self.image.get_width() < WIDTH // 2:
            self.image = pg.transform.scale(
                self.image,
                (self.image.get_width() * 1.05, self.image.get_height() * 1.05)
            )

        # Get the next hitbox
        old_x, old_y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = old_x, old_y

class Food(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/food.png")
        self.image = pg.transform.scale(
            self.image,
            (self.image.get_width() // 2, self.image.get_height() // 2)
        )
        self.rect = self.image.get_rect()

        # TODO: Spawn them in random locations

         # Randomize initial location
       
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

class Hawk(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/hawk.png")
        self.image = pg.transform.scale(
            self.image,
            (self.image.get_width() // 2, self.image.get_height() // 2)
        )
        self.rect = self.image.get_rect()

        # Randomize initial location
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

        self.vel_x = random.choice([-6, -5, -4, 4, 5, 6])
        self.vel_y = random.choice([-6, -5, -4, 4, 5, 6])

    def update(self):
        """Move the hawk side to side"""
        self.rect.x += self.vel_x

        # Bounce off the sides of the screen
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.vel_x = -self.vel_x

def display_game_over(screen): 
    font_game_over = pg.font.SysFont("Impact, 100")
    game_over_text = font_game_over.rect("Game Over", True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_text, game_over_rect)
    pg.display.flip()

def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    score = 0
    collison_count = 0 
   
    font = pg.font.SysFont("Impact", 20)
    
    # Sprite Groups
    all_sprites = pg.sprite.Group()
    Food_sprites = pg.sprite.Group()
    Hawk_sprites = pg.sprite.Group() 

    player = Player()
    all_sprites.add(player)
    

    # Create Food objects
    for _ in range(NUM_Food):
        food = Food()

        all_sprites.add(food)
        Food_sprites.add(food)
    
    
   # Create Hawk objects
    for _ in range(NUM_Hawk):
        hawk = Hawk()

        all_sprites.add(hawk)
        Hawk_sprites.add(hawk)
    
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # Update all sprites
        all_sprites.update()

        # Check for collsion with food 
        food_collided = pg.sprite.spritecollide(player, Food_sprites, True)
        for food in food_collided:
            # Increase the score by 10 
            score += 10

            player.grow()

            print(f"Score: {score}")

            # If the coin_sprites group is empty, respawn all coins
            if len(Food_sprites) <= 0:
                for _ in range(NUM_Food):
                    food = Food()

                    all_sprites.add(food)
                    Food_sprites.add(food)
    

        # Check for collison between Snake and Hawk 
        Hawk_collided = pg.sprite.spritecollide(player, Hawk_sprites, False)
        for hawk in Hawk_collided: 
            collison_count += 1
            if collison_count >= 100: 
                print("GAME OVER")
                done = True 

        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Render score and lives 
        score_image = font.render(f"Score: {score}", True, WHITE) 
        lives_image = font.render(f"Lives: {int(100 - collison_count)}", True, WHITE)

        # "Blit" the surface on the screen 
        screen.blit(score_image, (5, 5))
        screen.blit(lives_image, (5, 35))

        # if collison_count >= 100:
        #     while True:
        #         for event in pg.event.get():
        #             if event.type == pg.QUIT:
        #                 done = True

        #         display_game_over(screen) 

        pg.display.flip()
        clock.tick(60)
    
def main():
    start()


if __name__ == "__main__":
    main()


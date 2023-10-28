import pygame
import random

import os
os.environ["SDL_VIDEODRIVER"] = "windib"  # Required for Pygame window to display properly in VSCode
# Initialize Pygame
pygame.init()

# Set the width and height of the game window
WIDTH = 800
HEIGHT = 600

# Set the title of the game window
pygame.display.set_caption("Endless Runner Game")

# Set up the clock to manage the game's FPS
clock = pygame.time.Clock()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the player image
player_image = pygame.image.load("graphics/player.png").convert_alpha()

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        # Move the player left or right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# Load the obstacle image
obstacle_image = pygame.image.load("graphics/green.png").convert_alpha()

# Define the obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacle_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = 5

    def update(self):
        # Move the obstacle down the screen
        self.rect.y += self.speed

# Create sprite groups for the player and obstacles
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
obstacles = pygame.sprite.Group()

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn obstacles
    if random.randint(1, 60) == 1:
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    # Update sprites
    all_sprites.update()

    # Check for collisions
    if pygame.sprite.spritecollide(player, obstacles, False):
        running = False

    # Draw the screen
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    # Update the display
    pygame.display.update()

    # Tick the clock to control the game's FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()

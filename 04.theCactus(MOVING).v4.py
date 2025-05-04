"""
Author: Millie Young
Date: May 2025
'The Llama Game' assigned by P.Baker
"""

# Import the correct python pakages
import pygame
import sys
import time
import random

# Initiate the game
pygame.init()

# Set up display and game screen
screen = pygame.display.set_mode((800, 600))
game_icon = pygame.image.load('llama_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption('Lllama Run - By Millie Young')

# Fonts
exit_font = pygame.font.SysFont('arialblack', 30)
message_font = pygame.font.SysFont('arialblack', 30)

# Load and scale the background image
background = pygame.image.load('ground.png')
background = pygame.transform.scale(background, (800, 600))
llama = pygame.transform.scale(pygame.image.load('Llama.png'),(48, 64))
cactus = pygame.transform.scale(pygame.image.load('cactus.png'), (40, 55))

# Getting the Llama and initialize the rectangle for the Lllama
x_position, y_position = 400, 320
llama_rect = llama.get_rect(center=(x_position, y_position))

# Jumping parameters
y_gravity = 1
jump_height = 20
y_velocity = 0
landing_correction = 30

jumping = False    # Default of llama NOT jumping

# Score set up
clock = pygame.time.Clock()
score_font = pygame.font.SysFont('arialblack', 20)
start_time = pygame.time.get_ticks()  # Track the starting time

# Cactus Settings
cactus_list = []
cactus_spawn_time = 0
cactus_speed = 5  # This will be the speed at which the cactus will 'move' towards the llama
cactus_y = 352


# Creating the cactus spawning function.
# This will happen by cactus spawning outside the visible game frame and then 'moving' in
def spawn_cactus():
    cactus_x = random.randint(820, 1000) # Off screen as the screen dimensions are 800 x 600

    cactus_rect = cactus.get_rect(midbottom=(cactus_x, cactus_y))
    cactus_list.append(cactus_rect)

# Player presses space bar ('jump')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not jumping:
            jumping = True
            y_velocity = -jump_height

    # Calculate score based off of the time that the player has played the game for
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    score_text = score_font.render(f'Score: {elapsed_time}', True, (255, 255, 255))

    # Apply gravity
    if jumping:
        llama_rect.y += y_velocity
        y_velocity += y_gravity
        if llama_rect.y >= y_position - landing_correction:  # Stop when reaching initial position
            llama_rect.y = y_position - landing_correction
            jumping = False

    # Spawn cactus intervals
    if pygame.time.get_ticks() - cactus_spawn_time > 2000: # Spawn every two seconds
        spawn_cactus()
        cactus_spawn_time = pygame.time.get_ticks()

    # Move cactus towards Llama
    for cactus_rect in cactus_list:
        cactus_rect.x -= cactus_speed # Move to the left

    # Remove cactus that go off the players visible screen
    cactus_list = [c for c in cactus_list if c.x > -50]
    # NOTE: this is list comprehension which means that for each cactus in cactus list check if the x > -50

    # Render GAME
    screen.fill((0, 0, 0))  # Clear screen of the llama copies

    screen.blit(background, (0, 0))
    screen.blit(llama, llama_rect)
    screen.blit(score_text, (10, 10))  # Display score in top-left corner

    # Render in Cactus
    for cactus_rect in cactus_list:
        screen.blit(cactus, cactus_rect)

    pygame.display.update()
    clock.tick(60)

# End game
pygame.quit()
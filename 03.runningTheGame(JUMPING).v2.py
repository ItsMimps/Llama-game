import pygame
import sys
import time
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
game_icon = pygame.image.load('llama_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption('Lllama Run - By Millie Young')

clock = pygame.time.Clock()

# fonts
score_font = pygame.font.SysFont('arialblack', 30)
exit_font = pygame.font.SysFont('arialblack', 30)
message_font = pygame.font.SysFont('arialblack', 30)

# Load and scale the background image
background = pygame.image.load('ground.png')
background = pygame.transform.scale(background, (800, 600))
llama = pygame.transform.scale(pygame.image.load('Llama.png'),(48, 64))

# Getting the Llama AND initialize the rectangle for the Lllama

x_position, y_position = 400, 320
llama_rect = llama.get_rect(center=(x_position, y_position))

# Jumping parameters

y_gravity = 1
jump_height = 20
y_velocity = 0
jumping = False

ground_y = 320 # Establishing that the ground is at y-level 320

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not jumping:
            jumping = True
            y_velocity = -jump_height

    screen.blit(background, (0, 0))
    screen.blit(llama, llama_rect)

    # Applying the sense of 'gravity'

    if jumping:
        llama_rect.y += y_velocity
        y_velocity += y_gravity
        if llama_rect.y >= ground_y: # Making sure that the Llama stops when they 'hit' the ground
            llama_rect.y = ground_y
            jumping = False

    else:
        if y_velocity < -jump_height:
            jumping = False
            y_velocity = jump_height

    pygame.display.update()
    clock.tick(60)

pygame.quit()

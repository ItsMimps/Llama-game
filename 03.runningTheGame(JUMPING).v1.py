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

# Getting the Llama

x_position, y_position = 400, 320

# Jumping stuff

y_gravity = 1
jump_height = 20
y_velocity = jump_height

jumping = False

# Initialize the rectangle for the Lllama

llama_rect = llama.get_rect(center=(x_position, y_position))
is_jumping = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
        jumping = True

    screen.blit(background, (0, 0))
    screen.blit(llama, llama_rect)

    # Fill background and Llama in its rectangle position
    screen.blit(background, (0, 0))

    if jumping:
        y_position -= y_velocity
        y_velocity -= y_gravity
        if y_velocity < -jump_height:
            jumping = False
            y_velocity = jump_height
        else:
            llama_rect = llama.get_rect(center=(x_position, y_position))
            screen.blit(llama, llama_rect)

    llama_rect = llama.get_rect(center=(x_position, y_position))
    screen.blit(llama, llama_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
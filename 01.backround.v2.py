import pygame
import sys
import time
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
game_icon = pygame.image.load('llama_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption('Lllama Run - By Millie Young')

# Load and scale the background image

background = pygame.image.load('ground.png')
background = pygame.transform.scale(background, (800, 600))

clock = pygame.time.Clock()

# fonts
score_font = pygame.font.SysFont('arialblack', 30)
exit_font = pygame.font.SysFont('arialblack', 30)
message_font = pygame.font.SysFont('arialblack', 30)

quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        # draw background
    screen.blit(background, (0, 0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

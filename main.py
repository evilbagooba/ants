import pygame
import numpy as np
from environment import Environment
from critter import LangAnt
RED = (255, 0, 0)
WHITE = (255,255,255)
BLACK = (0,0,0)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
GRID_WIDTH, GRID_HEIGHT = 80, 80
CELL_SIZE = 10

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ants!")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

def initialize_ant():
    ant = LangAnt(GRID_WIDTH // 2, GRID_HEIGHT // 2, 0)  # Use integer division
    return ant

running = True

env = Environment(GRID_WIDTH, GRID_HEIGHT)
ant = initialize_ant()
frame_counter = 0
screen.fill(WHITE)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ant.move(env)


    screen.fill(WHITE)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if env.grid[y, x] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)

    pygame.draw.rect(screen, RED, (ant.x * CELL_SIZE, ant.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
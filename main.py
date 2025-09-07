import pygame
import pygame_menu
from pygame_menu import themes
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
def startSim():
    mainLoop(selected_rule)

RULE_INPUT_ID = "rule_input"

def rule_onchange(value):
    global selected_rule
    upper = value.upper()
    if value != upper:
        rule_widget = mainMenu.get_widget(RULE_INPUT_ID)
        rule_widget.set_value(upper)
    selected_rule = upper

mainMenu = pygame_menu.Menu("Ants!", SCREEN_WIDTH, SCREEN_HEIGHT, theme=themes.THEME_DEFAULT)
mainMenu.add.text_input(
    "Rule:",
    default="LR",
    copy_paste_enable=True,
    valid_chars=["L", "N", "R", "l", "n", "r"],
    onchange=rule_onchange,
    textinput_id=RULE_INPUT_ID
)

mainMenu.add.button("Start", startSim)
mainMenu.add.button("Quit",pygame_menu.events.EXIT)


def initialize_ant(ruleBits):
    ant = LangAnt(GRID_WIDTH // 2, GRID_HEIGHT // 2, 0)  # Use integer division
    print(ruleBits)
    return ant

def mainLoop(rule):
    env = Environment(GRID_WIDTH, GRID_HEIGHT)
    ruleBits = [{'L': -1, 'R': 1, 'N': 0}.get(char) for char in rule]
    ant = initialize_ant(ruleBits)
    actionCount = 0
    running = True

    screen.fill(WHITE)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        ant.move(env)
        actionCount += 1 

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
    exit()

selected_rule = "LR"  # Default value

if __name__ == "__main__":
    mainMenu.mainloop(screen)
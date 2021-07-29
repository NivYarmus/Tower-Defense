import pygame
from math import ceil

import Draw.constants as constants
from Draw.Interactions.Types.DartMonkeyButton import DartMonkeyButton
from Draw.Interactions.Types.BombTowerButton import BombTowerButton


pygame.font.init()
window = None
font = pygame.font.SysFont('arial', 12)
font2 = pygame.font.SysFont('arial', 30)
font3 = pygame.font.SysFont('arial', 20)

Dart_Monkey_Button = DartMonkeyButton(constants.CHARACTER_MENU_X, constants.CHARACTER_MENU_Y, constants.CHARACTER_WIDTH, constants.CHARACTER_HEIGHT)
Bomb_Tower_Button = BombTowerButton(constants.CHARACTER_MENU_X, constants.CHARACTER_MENU_Y + constants.CHARACTER_HEIGHT, constants.CHARACTER_WIDTH, constants.CHARACTER_HEIGHT)
CHARACTER_BUTTONS = [Dart_Monkey_Button, Bomb_Tower_Button]


def create_window():
    """
    Create the game window
    None -> None
    """
    global window
    window = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    pygame.display.set_caption('Ballons TD')


def draw_maps(game_map):
    """
    Draw the game maps
    list -> None
    """
    for i in range(len(game_map.grid)):
        for j in range(len(game_map.grid[i])):
            window.blit(pygame.transform.scale(game_map.string_to_image(game_map.grid[i][j]), (constants.TILE_WIDTH, constants.TILE_HEIGHT)), (constants.MAP1_X + constants.TILE_WIDTH * j, constants.MAP_Y + constants.TILE_HEIGHT * i))
            window.blit(pygame.transform.scale(game_map.string_to_image(game_map.grid[i][j]), (constants.TILE_WIDTH, constants.TILE_HEIGHT)), (constants.MAP2_X + constants.TILE_WIDTH * j, constants.MAP_Y + constants.TILE_HEIGHT * i))


def draw_monkeys(monkeys1, monkeys2):
    """
    Draw the monkeys of both competitors
    list, list -> None
    """
    def draw_monkeys1():
        for monkey in monkeys1:
            window.blit(pygame.transform.scale(monkey.string_to_image(monkey.image), (constants.TILE_WIDTH, constants.TILE_HEIGHT)), (constants.MAP1_X + constants.TILE_WIDTH * monkey.x, constants.MAP_Y + constants.TILE_HEIGHT * monkey.y))
    def draw_monkeys2():
        for monkey in monkeys2:
            window.blit(pygame.transform.scale(monkey.string_to_image(monkey.image), (constants.TILE_WIDTH, constants.TILE_HEIGHT)), (constants.MAP2_X + constants.TILE_WIDTH * monkey.x, constants.MAP_Y + constants.TILE_HEIGHT * monkey.y))
    draw_monkeys1()
    draw_monkeys2()


def draw_balloons(balloons1, balloons2):
    """
    Draw the balloons of both competitors
    list, list -> None
    """
    def draw_balloons1():
        for balloon in balloons1:
            if balloon.x >= 0:
                window.blit(pygame.transform.scale(balloon.string_to_image(balloon.image), (constants.TILE_WIDTH, constants.TILE_HEIGHT)), (constants.MAP1_X + constants.TILE_WIDTH * balloon.x, constants.MAP_Y + constants.TILE_HEIGHT * balloon.y))
    def draw_balloons2():
        for balloon in balloons2:
            if balloon.x >= 0:
                window.blit(pygame.transform.scale(balloon.string_to_image(balloon.image), (constants.TILE_WIDTH, constants.TILE_HEIGHT)), (constants.MAP2_X + constants.TILE_WIDTH * balloon.x, constants.MAP_Y + constants.TILE_HEIGHT * balloon.y))
    draw_balloons1()
    draw_balloons2()


def draw_money(money):
    """
    Draw the amount of money the player has
    int -> None
    """
    msg = font.render(f'${money}', True, (255, 255, 255), None)
    window.blit(msg, (constants.MONEY_X, constants.MONEY_Y))


def draw_wave(level):
    """
    Draw the current level the game is at
    int -> None
    """
    msg = font.render(f'Wave #{level}', True, (255, 255, 255), None)
    window.blit(msg, (constants.WAVE_X, constants.WAVE_Y))


def draw_character_menu():
    def draw_characters():
        for button in CHARACTER_BUTTONS:
            msg = font3.render(f'${button.cost}', True, (255, 255, 255), None)
            window.blit(pygame.transform.scale(button.image, (button.width, button.height)), (button.x, button.y))
            window.blit(msg, (button.x, button.y + button.height - msg.get_height() - 1))
    """
    Draw the character buy menu and draw the characters inside the character menu
    None -> None
    """
    window.blit(pygame.transform.scale(constants.CHARACTER_MENU_IMAGE, (constants.CHARACTER_MENU_WIDTH, constants.CHARACTER_MENU_HEIGHT)), (constants.CHARACTER_MENU_X, constants.CHARACTER_MENU_Y))
    draw_characters()


def draw_partition():
    """
    Draw the partition between the two maps
    None -> None
    """
    window.blit(pygame.transform.scale(constants.PARTITION_IMAGE, (constants.PARTITION_WIDTH, constants.PARTITION_HEIGHT)), (constants.PARTITION_X, constants.PARTITION_Y))


def draw_health_bars(health1, health2, full_health1, full_health2):
    """
    Draw the health bars of both competitors
    int, int, int, int -> None
    """
    def draw_health_bar_map1():
        health_space = ceil((health1 / full_health1) * constants.MAP_WIDTH)
        if health_space < 0:
            health_space = 0
        missing_health_space = constants.MAP_WIDTH - health_space
        if health_space > 0:
            pygame.draw.rect(window, (0, 255, 0), (constants.HEALTH1_X, constants.HEALTH_Y, health_space, constants.HEALTH_HEIGHT))
        if missing_health_space > 0:
            pygame.draw.rect(window, (255, 0, 0), (constants.HEALTH1_X + health_space, constants.HEALTH_Y, missing_health_space, constants.HEALTH_HEIGHT))
        msg = font2.render(str(health1), True, (255, 255, 255), None)
        window.blit(msg, (constants.CHARACTER_MENU_WIDTH, 0))
    def draw_health_bar_map2():
        health_space = ceil((health2 / full_health2) * constants.MAP_WIDTH)
        if health_space < 0:
            health_space = 0
        missing_health_space = constants.MAP_WIDTH - health_space
        if health_space > 0:
            pygame.draw.rect(window, (0, 255, 0), (constants.HEALTH2_X, constants.HEALTH_Y, health_space, constants.HEALTH_HEIGHT))
        if missing_health_space > 0:
            pygame.draw.rect(window, (255, 0, 0), (constants.HEALTH2_X + health_space, constants.HEALTH_Y, missing_health_space, constants.HEALTH_HEIGHT))
        msg = font2.render(str(health2), True, (255, 255, 255), None)
        window.blit(msg, (constants.MAP2_X, 0))
    draw_health_bar_map1()
    draw_health_bar_map2()



def draw_button(x, y, image):
    """
    Draw an image onto the screen
    int, int, pygame.Image -> None
    """
    window.blit(pygame.transform.scale(image, (constants.TILE_WIDTH, constants.TILE_HEIGHT)), (constants.MAP1_X + constants.TILE_WIDTH * x, constants.MAP_Y + constants.TILE_HEIGHT * y))


def draw_victory_screen():
    """
    Draw the victory screen
    None -> None
    """
    window.blit(pygame.transform.scale(constants.VICTORY_IMAGE, (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)), (0, 0))


def draw_defeat_screen():
    """
    Draw the defeat screen
    None -> None
    """
    window.blit(pygame.transform.scale(constants.DEFEAT_IMAGE, (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)), (0, 0))

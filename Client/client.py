import pygame

import Draw.Draw as Graphics
from Networking.network import Network
from Protocol.constants import QUIT_GAME_PROTOCOL
from Protocol.protocol_handler import handle_server_message, create_message
from Draw.Interactions.map_interactions import check_if_in_map1, get_map1_coordinates


network = Network()


def draw_in_loop(game1, game2):
    Graphics.draw_maps(game1.map)
    Graphics.draw_monkeys(game1.monkeys, game2.monkeys)
    Graphics.draw_balloons(game1.balloons, game2.balloons)
    Graphics.draw_partition()
    Graphics.draw_character_menu()
    Graphics.draw_money(game1.money)
    Graphics.draw_wave(game1.level)
    Graphics.draw_health_bars(game1.health, game2.health, game1.full_health, game2.full_health)


def check_pygame_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def handle_mouse_interactions(marked):
    protocol, coordinates = None, None
    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]: # check if the player press the left mouse button
        if marked is None:
            for button in Graphics.CHARACTER_BUTTONS: # check if the player pressed a button
                if button.is_pressed(x, y):
                    marked = button
                    break
        else:
            if check_if_in_map1(x, y): # check if the player wants to purchase the monkey
                coordinates = get_map1_coordinates(x, y)
                protocol = marked.monkey
                marked = None
    return marked, protocol, coordinates


def draw_marked_monkey(marked):
    if marked is not None:
        x, y = pygame.mouse.get_pos()
        if check_if_in_map1(x, y):
            x, y = get_map1_coordinates(x, y)
            Graphics.draw_button(x, y, marked.image)


def main():
    global network
    try:
        network.connect() # connect to the server
    except Exception as e:
        print(e)
    else:
        game1, game2 = handle_server_message(network.receive()) # get the starting map border

        run = True
        marked = None
        FPS = 200
        clock = pygame.time.Clock()

        Graphics.create_window()

        while run and game1.health > 0 and game2.health > 0: # while no-one lost and the player did not quit
            if check_pygame_close(): # check if the player wants to quit
                network.send(QUIT_GAME_PROTOCOL)
                run = False

            clock.tick(FPS)
            draw_in_loop(game1, game2) # draw all game objects

            marked, monkey, coordinates = handle_mouse_interactions(marked) # check if the player has made an interaction
            draw_marked_monkey(marked)

            network.send(create_message(monkey, coordinates))

            data = network.receive()
            if not data: # check if the server is offline
                break
            game1, game2 = handle_server_message(data)

            pygame.display.flip()

        network.close()

        if game1.health <= 0:
            Graphics.draw_defeat_screen()
        elif game2.health <= 0:
            Graphics.draw_victory_screen()
        pygame.display.flip()

        while run:
            if check_pygame_close():
                run = False


if __name__ == '__main__':
    main()

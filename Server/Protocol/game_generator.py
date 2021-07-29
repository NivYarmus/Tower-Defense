from Game.Game import Game
from Map.Map import Map
from Map.Types.Spring_Map import SPRING_MAP_GRID, SPRING_MAP_PATH

from random import choice


MAPS = [(SPRING_MAP_GRID, SPRING_MAP_PATH)]


def create_game():
    """
    Create the Game object of the competitors
    None -> Game, Game
    """
    map = choice(MAPS)
    game1, game2 = Game(Map(map[0], map[1])), Game(Map(map[0], map[1]))
    return game1, game2

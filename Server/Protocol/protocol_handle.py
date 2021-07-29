from pickle import loads, dumps

import Protocol.constants as constants
from ClientGame.game import Game
from Monkeys.Types.Dart_Monkey import DartMonkey
from Monkeys.Types.Bomb_Tower import BombTower


MONKEYS = {constants.BOUGHT_DART_MONKEY_PROTOCOL: DartMonkey, constants.BOUGHT_BOMB_TOWER_PROTOCOL: BombTower}


def break_message(data):
    """
    Split the client message to the protocol type & data
    bytes -> bytes, bytes
    """
    return data[:constants.CLIENT_PROTOCOL_TYPE_FIELD_LENGTH], data[constants.CLIENT_PROTOCOL_TYPE_FIELD_LENGTH:]


def handle_client_message(game, protocol, data):
    """
    Handle the protocol request that was sent by the client
    Game, bytes, bytes -> None
    """
    if protocol in MONKEYS.keys():
        monkey, coordinates = MONKEYS[protocol], loads(data)
        x, y = coordinates
        coordinates = (y, x)
        for m in game.monkeys:
            if x == m.x and y == m.y:
                return None
        if coordinates not in game.map.path:
            m = monkey(x, y)
            if game.money >= m.cost:
                game.monkeys.append(m)
                game.money -= m.cost
                m.start_shotting(game)


def create_message(g):
    """
    Create a message to send to the client according to the protocol
    Tuple<Game, Game> -> bytes
    """
    game1, game2 = g
    g = [Game(game1), Game(game2)]
    return dumps(g)

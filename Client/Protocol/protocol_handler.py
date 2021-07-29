from pickle import loads, dumps

from Protocol.constants import NO_CHANGE_PROTOCOL


def handle_server_message(data):
    """
    Handle the message from the server
    bytes -> Game, Game
    """
    games = loads(data)
    return games[0], games[1]


def create_message(monkey = None, coordinates = None):
    """
    Create a message to send to the Server
    bytes, Tuple<int, int> -> bytes
    """
    if monkey is not None:
        return monkey + dumps(coordinates)
    return NO_CHANGE_PROTOCOL

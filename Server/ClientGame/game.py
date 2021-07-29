from ClientGame.Object import Character
from ClientGame.Map import Map


class Game:
    def __init__(self, game):
        """
        A copy of the Game object that will be transfered to the client
        Game -> None
        """
        self.full_health = game.full_health
        self.health = game.health
        self.money = game.money
        self.map = Map(game.map)
        self.level = game.wave.level
        self.monkeys = list(Character(m.x, m.y, m.image) for m in game.monkeys)
        self.balloons = list(Character(b.x, b.y, b.image) for b in game.wave.balloons)
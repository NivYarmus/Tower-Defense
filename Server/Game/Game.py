from Game.constants import PLAYER_HEALTH, START_MONEY
from Wave.Wave import Wave


class Game:
    def __init__(self, game_map):
        """
        list -> None
        """
        self.full_health = PLAYER_HEALTH
        self.health = PLAYER_HEALTH
        self.map = game_map
        self.wave = Wave(game_map.path)
        self.money = START_MONEY
        self.monkeys = list()
        self.running = True

    def stop_game(self):
        """
        terminates all monkeys and balloons threads
        None -> None
        """
        for monkey in self.monkeys:
            monkey.stop_shotting()

        for balloon in self.wave.balloons:
            balloon.stop_moving()

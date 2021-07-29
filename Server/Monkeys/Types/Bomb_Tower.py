from Monkeys.Monkey import Monkey
from Monkeys.Types.Constants import BOMB_TOWER_ATTACK_SPEED, BOMB_TOWER_RANGE, EXPLOTION_RANGE, BOMB_TOWER_COST, BOMB_TOWER_IMAGE
from math import sqrt


class BombTower(Monkey):
    def __init__(self, x, y):
        super().__init__(x, y, BOMB_TOWER_COST, BOMB_TOWER_ATTACK_SPEED, BOMB_TOWER_RANGE, BOMB_TOWER_IMAGE)
        self.explotion_range = EXPLOTION_RANGE

    def get_balloons_in_range(self, balloons):
        """
        Find all balloons in the blast range of the targeted balloon
        list -> list
        """
        balloons = self.find_balloons_in_range(balloons)
        if len(balloons) > 0:
            first_balloon = balloons[0]
            balloons = list(filter(lambda balloon: sqrt(pow(balloon.x - first_balloon.x, 2) + pow(balloon.y - first_balloon.y, 2)) <= self.explotion_range, balloons))
            if len(balloons) > 0:
                balloons.append(first_balloon)
                return balloons
        return None

    def shot_balloon(self, player):
        self._lock.acquire()
        balloons = self.get_balloons_in_range(player.wave.balloons)
        if balloons is not None:
            self.rotate_image_to_balloon(balloons[0])
            for ballon in balloons:
                ballon.health -= 1
                if ballon.health == 0:
                    player.money += ballon.cash
                    ballon.stop_moving()
                    player.wave.balloons.remove(ballon)
        self._lock.release()

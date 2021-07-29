from Monkeys.Monkey import Monkey
from Monkeys.Types.Constants import DART_MONKEY_ATTACK_SPEED, DART_MONKEY_IMAGE, DART_MONKEY_RANGE, DART_MONKEY_COST


class DartMonkey(Monkey):
    def __init__(self, x, y):
        super().__init__(x, y, DART_MONKEY_COST, DART_MONKEY_ATTACK_SPEED, DART_MONKEY_RANGE, DART_MONKEY_IMAGE)

    def choose_lowest_health_balloons(self, balloons):
        """
        Choose the ballon with the least amount on health from all the balloons with are in range
        list -> Ballon
        """
        balloons = sorted(balloons, key=lambda balloon: balloon.health)
        if len(balloons) > 0:
            return balloons[0]
        return None

    def shot_balloon(self, player):
        self._lock.acquire()
        balloon = self.choose_lowest_health_balloons(self.find_balloons_in_range(player.wave.balloons))
        if balloon is not None:
            self.rotate_image_to_balloon(balloon)
            balloon.health -= 1
            if balloon.health == 0:
                player.money += balloon.cash
                balloon.stop_moving()
                player.wave.balloons.remove(balloon)
        self._lock.release()

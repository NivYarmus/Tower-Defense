from pygame import transform
from threading import Timer, Lock
from math import sqrt, atan2, degrees
from abc import ABC, abstractmethod


class Monkey(ABC):
    def __init__(self, x, y, cost, shots_per_second, radius, image):
        """
        int, int, int, float, int, pygame.Image -> None
        """
        self.x = x
        self.y = y
        self.cost = cost
        self.range = radius
        self.shot_delay = 1 / shots_per_second
        self.image = image
        self._start_image = image
        self._lock = Lock()

    def rotate_image_to_balloon(self, balloon):
        """
        Rotate the monkey towards the balloon he is shotting at
        Ballon -> None
        """
        angle = degrees(atan2(self.y - balloon.y, balloon.x - self.x)) - 90
        self.image = transform.rotate(self._start_image, angle)

    def find_balloons_in_range(self, balloons):
        """
        Find all balloons in range of the monkey
        list -> list
        """
        return list(filter(lambda balloon: sqrt(pow(balloon.x - self.x, 2) + pow(balloon.y - self.y, 2)) <= self.range, balloons))

    @abstractmethod
    def shot_balloon(self, player):
        """
        Shot once
        Game -> None
        """
        pass

    def start_shotting(self, player):
        """
        Start shotting balloons
        Game -> None
        """
        Timer(self.shot_delay, self.__shot_loop, args=((player,))).start()

    def stop_shotting(self):
        """
        Stop shotting balloons
        None -> None
        """
        self._thread.cancel()
        self._thread.join()

    def __shot_loop(self, player):
        """
        Shot balloons in a loop
        Game -> None
        """
        self._thread = Timer(self.shot_delay, self.__shot_loop, args=((player,)))
        self._thread.start()
        self.shot_balloon(player)

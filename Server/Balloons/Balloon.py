from threading import Timer, Lock


class Balloon:
    def __init__(self, health, path, movement_speed, cash, image):
        """
        int, list, float, int, pygame.Image -> None
        """
        self.x = path[0][1]
        self.y = path[0][0]
        self.health = health
        self.path = path[1:]
        self.cash = cash
        self.movement_delay = 1 / movement_speed
        self.image = image
        self._lock = Lock()

    def start_moving(self, player):
        """
        Starts the movement of the balloon
        Game -> None
        """
        Timer(self.movement_delay, self.__move_loop, args=((player,))).start()

    def stop_moving(self):
        """
        Stops the movement of the balloon
        None -> None
        """
        try:
            self._thread.cancel()
            self._thread.join()
        except:
            pass

    def __move_loop(self, player):
        """
        Moves the balloon in a loop
        Game -> None
        """
        self._thread = Timer(self.movement_delay, self.__move_loop, args=((player,)))
        self._thread.start()
        self.move(player)

    def move(self, player):
        """
        Move the balloon a single step
        Game -> None
        """
        self._lock.acquire()
        if len(self.path) > 0:
            self.x = self.path[0][1]
            self.y = self.path[0][0]
            self.path.pop(0)
        elif self.health <= 0:
            self.stop_moving()
        else:
            player.health -= self.health
            player.wave.balloons.remove(self)
            self.stop_moving()
        self._lock.release()

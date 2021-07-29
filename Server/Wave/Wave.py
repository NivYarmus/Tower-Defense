from Balloons.Types.Red_Balloon import RedBalloon
from Wave.Constants import BALLOONS_ADDED_PER_WAVE


class Wave:
    def __init__(self, wave_path):
        """
        list -> None
        """
        self.level = 0
        self.path = wave_path
        self.balloons_per_wave = BALLOONS_ADDED_PER_WAVE
        self.balloons_count = 0
        self.balloons = list()

    def next_wave(self, player):
        """
        Summons the next wave of balloons
        Game -> None
        """
        self.level += 1
        self.balloons_count += self.balloons_per_wave
        y, x = self.path[0]
        for i in range(self.balloons_count):
            path = list((y, x - j - 1) for j in range(i))[::-1] + self.path
            self.balloons.append(RedBalloon(path))
            self.balloons[-1].start_moving(player)

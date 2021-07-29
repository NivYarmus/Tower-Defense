from Balloons.Balloon import Balloon
from Balloons.Types.constants import RED_BALLOON_CASH, RED_BALLOON_HEALTH, RED_BALLOON_IMAGES, RED_BALLOON_SPEED


class RedBalloon(Balloon):
    def __init__(self, path):
        """
        list -> None
        """
        super().__init__(RED_BALLOON_HEALTH, path, RED_BALLOON_SPEED, RED_BALLOON_CASH, RED_BALLOON_IMAGES)

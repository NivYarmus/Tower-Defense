from Draw.Interactions.Character_Button import CharacterButton
from Draw.Interactions.Types.constants import BOMB_TOWER_COST, BOMB_TOWER_IMAGE
from Protocol.constants import BOMB_TOWER_PROTOCOL


class BombTowerButton(CharacterButton):
    def __init__(self, x, y, width, height):
        """
        int, int, int, int -> None
        """
        super().__init__(x, y, width, height, BOMB_TOWER_IMAGE, BOMB_TOWER_COST, BOMB_TOWER_PROTOCOL)

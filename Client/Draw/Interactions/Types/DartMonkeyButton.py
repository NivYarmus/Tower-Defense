from Draw.Interactions.Character_Button import CharacterButton
from Draw.Interactions.Types.constants import DART_MONKEY_COST, DART_MONKEY_IMAGE
from Protocol.constants import DART_MONKEY_PROTOCOL


class DartMonkeyButton(CharacterButton):
    def __init__(self, x, y, width, height):
        """
        int, int, int, int -> None
        """
        super().__init__(x, y, width, height, DART_MONKEY_IMAGE, DART_MONKEY_COST, DART_MONKEY_PROTOCOL)

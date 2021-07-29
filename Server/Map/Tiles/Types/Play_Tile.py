from Map.Tiles.Tile import Tile
from Map.Tiles.Types.constants import PLAY_TILE_IMAGE


class PlayTile(Tile):
    def __init__(self):
        """
        None -> None
        """
        super().__init__(PLAY_TILE_IMAGE)

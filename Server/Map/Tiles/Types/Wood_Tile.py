from Map.Tiles.Tile import Tile
from Map.Tiles.Types.constants import WOOD_TILE_IMAGE


class WoodTile(Tile):
    def __init__(self):
        """
        None -> None
        """
        super().__init__(WOOD_TILE_IMAGE)

from Map.Tiles.Tile import Tile
from Map.Tiles.Types.constants import DIRT_TILE_IMAGE


class DirtTile(Tile):
    def __init__(self):
        """
        None -> None
        """
        super().__init__(DIRT_TILE_IMAGE)

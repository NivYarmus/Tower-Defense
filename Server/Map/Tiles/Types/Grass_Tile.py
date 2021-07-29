from Map.Tiles.Tile import Tile
from Map.Tiles.Types.constants import GRASS_TILE_IMAGE


class GrassTile(Tile):
    def __init__(self):
        """
        None -> None
        """
        super().__init__(GRASS_TILE_IMAGE)

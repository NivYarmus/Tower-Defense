from Map.Tiles.Tile import Tile
from Map.Tiles.Types.constants import LIGHT_WOOD_TILE_IMAGE


class LightWoodTile(Tile):
    def __init__(self):
        """
        None -> None
        """
        super().__init__(LIGHT_WOOD_TILE_IMAGE)

from Map.Tiles.Tile import Tile
from Map.Tiles.Types.constants import TREE_TILE_IMAGE


class TreeTile(Tile):
    def __init__(self):
        """
        None -> None
        """
        super().__init__(TREE_TILE_IMAGE)

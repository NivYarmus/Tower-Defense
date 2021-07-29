from Map.Tiles.Types.Tree_Tile import TreeTile
from Map.Tiles.Types.Dirt_Tile import DirtTile
from Map.Tiles.Types.Grass_Tile import GrassTile
from Map.Tiles.Types.Light_Wood_Tile import LightWoodTile
from Map.Tiles.Types.Wood_Tile import WoodTile
from Map.Tiles.Types.Play_Tile import PlayTile


SPRING_MAP_GRID = [
			[GrassTile(), TreeTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), TreeTile(), GrassTile(), GrassTile(), GrassTile(), TreeTile(), TreeTile(), GrassTile(), GrassTile(), GrassTile(), TreeTile(), GrassTile(), GrassTile(), WoodTile(), WoodTile()],
			[GrassTile(), GrassTile(), GrassTile(), TreeTile(), GrassTile(), TreeTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), TreeTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), WoodTile(), WoodTile()],
			[GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), TreeTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), TreeTile(), WoodTile(), WoodTile()],
			[GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), WoodTile(), WoodTile()],
			[DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), DirtTile(), WoodTile(), WoodTile()],
			[GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), WoodTile(), WoodTile()],
			[GrassTile(), TreeTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), TreeTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), WoodTile(), WoodTile()],
			[TreeTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), TreeTile(), GrassTile(), GrassTile(), GrassTile(), TreeTile(), TreeTile(), GrassTile(), GrassTile(), GrassTile(), TreeTile(), GrassTile(), GrassTile(), WoodTile(), WoodTile()],
			[GrassTile(), GrassTile(), GrassTile(), TreeTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), WoodTile(), WoodTile()],
			[LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), LightWoodTile(), PlayTile(), PlayTile()]
			]

SPRING_MAP_PATH = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4,11), (4, 12), (4, 13), (4, 14), (4, 15), (4, 16), (4, 17)]

from Map.Map import Map
from Map.Types.constants import SPRING_MAP_GRID, SPRING_MAP_PATH


class SpringMap(Map):
    def __init__(self):
        """
        None -> None
        """
        super().__init__(SPRING_MAP_GRID, SPRING_MAP_PATH)

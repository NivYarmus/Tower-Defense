from Draw.constants import MAP1_X, MAP_Y, MAP_WIDTH, WINDOW_HEIGHT, TILE_WIDTH, TILE_HEIGHT


def check_if_in_map1(x, y):
    """
    Check if coordinates are inside map #1
    int, int -> bool
    """
    return MAP1_X <= x < (MAP_WIDTH + MAP1_X) and MAP_Y <= y < WINDOW_HEIGHT


def get_map1_coordinates(x, y):
    """
    Get the position of the coordinates inside map #1
    int, int -> Tuple<int, int>
    """
    return ((x - MAP1_X) // TILE_WIDTH, y // TILE_HEIGHT)

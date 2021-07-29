from pygame.image import tostring


class Map:
    def __init__(self, map):
        """
        A copy of the Map object that will be transfered to the client
        list -> None
        """
        self.path = map.path
        self.width, self.height = map.grid[0][0].image.get_size()
        self.grid = list(list(self.image_to_string(tile.image) for tile in row) for row in map.grid)
    
    def image_to_string(self, img):
        """
        Turn an pygame.Image into a bytes array
        pygame.Image -> string
        """
        return tostring(img, 'RGBA')

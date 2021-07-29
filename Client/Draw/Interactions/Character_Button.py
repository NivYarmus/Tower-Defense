import Draw.constants as constants


class CharacterButton:
    def __init__(self, x, y, width, height, image, cost, monkey):
        """
        int, int, int, int, pygame.Image, int, bytes -> None
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.cost = cost
        self.monkey = monkey

    def is_pressed(self, x, y):
        """
        Check if the coordinates are inside the button area
        int, int -> bool
        """
        return self.x <= x < self.x + self.width and self.y <= y < self.y + self.height

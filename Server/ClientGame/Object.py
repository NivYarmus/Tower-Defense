from pygame.image import tostring


class Character:
    def __init__(self, x, y, img):
        """
        A copy of the Monkey/Balloon object that will be transfered to the client
        list -> None
        """
        self.x = x
        self.y = y
        self.width, self.height = img.get_size()
        self.image = self.image_to_string(img)
    
    def image_to_string(self, img):
        """
        Turn an pygame.Image into a bytes array
        pygame.Image -> string
        """
        return tostring(img, 'RGBA')

from pygame.image import fromstring


class Character:
    def string_to_image(self, img):
        """
        Turn a string into a pygame.Image object
        string -> pygame.Image
        """
        return fromstring(img, (self.width, self.height), 'RGBA')

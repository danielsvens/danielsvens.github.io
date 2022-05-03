import arcade
import PIL


class Grid(arcade.Sprite):

    def __init__(self, x, y, offset, name):
        super().__init__()
        self.name = name
        self.offset = offset
        self.position = (x, y)
        self.is_taken = False
        self.texture = self.create_texture()

    def create_texture(self):
        image = PIL.Image.new('RGBA', (self.offset, self.offset), arcade.color.GREEN)
        return arcade.Texture('rectangle', image=image)

    def claim(self):
        self.is_taken = True

import arcade
from .symbol_type import SymbolType


class Symbol(arcade.Sprite):

    def __init__(self, x, y, symbol_type):
        super().__init__()
        self.position = (x, y)
        self.draw = self.draw_x(x, y) if symbol_type == SymbolType.CROSS else self.draw_circle(x, y)

    @staticmethod
    def draw_x(x, y):
        arcade.draw_line(x, y, x + 45, y - 45, arcade.color.ORIOLES_ORANGE, 4)
        arcade.draw_line(x, y, x - 45, y + 45, arcade.color.ORIOLES_ORANGE, 4)
        arcade.draw_line(x, y, x + 45, y + 45, arcade.color.ORIOLES_ORANGE, 4)
        arcade.draw_line(x, y, x - 45, y - 45, arcade.color.ORIOLES_ORANGE, 4)

    @staticmethod
    def draw_circle(x, y):
        return arcade.draw_circle_outline(x, y, 50, arcade.color.ORIOLES_ORANGE, 4)

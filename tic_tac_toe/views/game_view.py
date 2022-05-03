import arcade

from tic_tac_toe.objects.grid import Grid
from tic_tac_toe.objects.symbol import Symbol
from tic_tac_toe.objects.symbol_type import SymbolType
from itertools import cycle

DARK_BLUE = (38, 70, 83)
PIXEL_OFFSET = 133


class GameView(arcade.View):

    def __init__(self, width, height):
        super().__init__()
        self.center_x = width // 2
        self.center_y = height // 2
        self.symbols = arcade.SpriteList()
        self.grid = arcade.SpriteList()
        self.symbol_cycle = cycle([SymbolType.CIRCLE, SymbolType.CROSS])

        self.coordinates = {
            'top-left': (self.center_x - PIXEL_OFFSET, self.center_y + PIXEL_OFFSET),
            'top-mid': (self.center_x, self.center_y + PIXEL_OFFSET),
            'top-right': (self.center_x + PIXEL_OFFSET, self.center_y + PIXEL_OFFSET),
            'mid-left': (self.center_x - PIXEL_OFFSET, self.center_y),
            'mid': (self.center_x, self.center_y),
            'mid-right': (self.center_x + PIXEL_OFFSET, self.center_y),
            'bottom-left': (self.center_x - PIXEL_OFFSET, self.center_y - PIXEL_OFFSET),
            'bottom-mid': (self.center_x, self.center_y - PIXEL_OFFSET),
            'bottom-right': (self.center_x + PIXEL_OFFSET, self.center_y - PIXEL_OFFSET)
        }

        self.setup()

    def setup(self):
        for k, v in self.coordinates.items():
            self.grid.append(Grid(*v, PIXEL_OFFSET, k))

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        arcade.start_render()

    def on_draw(self):
        self.draw_board()
        self.symbols.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        sprites = arcade.get_sprites_at_point((x, y), self.grid)

        if len(sprites):
            sprite: Grid = sprites[0]

            if not sprite.is_taken:
                self.symbols.append(Symbol(*sprite.position, self.symbol_cycle.__next__()))
                sprite.claim()

    def draw_dot(self):
        for dot in self.coordinates.values():
            arcade.draw_point(*dot, arcade.color.BLACK, 4)

    def draw_board(self):
        # self.draw_dot()
        arcade.draw_rectangle_outline(self.center_x, self.center_y, 400, 400, DARK_BLUE, 4)
        arcade.draw_line(self.center_x - 200, self.center_y - 66, 600, 234, DARK_BLUE, 4)
        arcade.draw_line(self.center_x + 200, self.center_y + 66, 200, 366, DARK_BLUE, 4)
        arcade.draw_line(self.center_x - 66, self.center_y - 200, 334, 500, DARK_BLUE, 4)
        arcade.draw_line(self.center_x + 66, self.center_y + 200, 466, 100, DARK_BLUE, 4)

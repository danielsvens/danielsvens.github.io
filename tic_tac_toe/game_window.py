import arcade

from tic_tac_toe.views.game_view import GameView


class GameWindow(arcade.Window):

    def __init__(self, width, height, screen, title):
        super().__init__(width, height, title)
        self.w = width
        self.h = height
        self._left = screen.width // 2 - self.w // 2
        self._top = screen.height // 2 - self.h // 2
        self.set_location(self._left, self._top)

    def setup(self):
        game_view = GameView(self.w, self.h)
        self.show_view(game_view)

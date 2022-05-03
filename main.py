import pyglet

from tic_tac_toe.game_window import GameWindow

GAME_WIDTH = 800
GAME_HEIGHT = 600
GAME_TITLE = 'TicTacToe'
SCREEN_NUM = 0
SCREENS = pyglet.canvas.Display().get_screens()
SCREEN = SCREENS[SCREEN_NUM]


def main():
    window = GameWindow(GAME_WIDTH, GAME_HEIGHT, SCREEN, GAME_TITLE)
    window.setup()
    window.run()


if __name__ == '__main__':
    main()

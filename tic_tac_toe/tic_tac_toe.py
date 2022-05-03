from objects.symbol_type import SymbolType


class TicTacToe:
    """ This logic is broken lelllll

    """

    def __init__(self):
        self.board = [SymbolType.CROSS for _ in range(3)]
        self.combinations = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]

    def check_win(self, pl):
        return all(pl == self.board[pos] for pos in [0, 1, 2])

    def check_draw(self):
        return ' ' in self.board


if __name__ == '__main__':
    t = TicTacToe()
    player: SymbolType = SymbolType.CROSS
    winner = t.check_win(player)

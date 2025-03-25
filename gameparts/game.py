class TicTacToeGame:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def get_board(self):
        print('-' * 5)
        for i in self.board:
            print('|'.join(i))
            print('-' * 5)
        print()    

    def get(self, col, row, player):
        self.board[col][row] = player
class TicTacToeGame:
    """Класс, который описывает игровое поле"""

    a = 3

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def get_board(self):
        print('-' * 5)
        for i in self.board:
            print('|'.join(i))
            print('-' * 5)
        print()

    def get(self, row, col, player):
        self.board[row][col] = player

    def game_over(self):
        for row in range(self.a):
            for col in range(self.a):
                if self.board[row][col] == ' ':
                    return False
        return True

    def check_win(self, player):
        # Проверка по горизонталям и вертикалям
        for i in range(self.a):
            if (all([self.board[i][j] == player for j in range(self.a)]) or
                    all([self.board[j][i] == player for j in range(self.a)])):
                return True

        # Проверка по диагоналям
        if (all([self.board[i][i] == player for i in range(self.a)]) or
            all([self.board[i][self.a - 1 - i] == player for
                i in range(self.a)])):
            return True

        return False

    def __str__(self):
        return ('Объект игрового поля размером '
                f'{self.a}x{self.a}')

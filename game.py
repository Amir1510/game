from gameparts.tic_tac_tor_game import TicTacToeGame
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def save_result(result):
    file = open('result.txt', 'a', encoding='utf-8')
    file.write(result + '\n')
    file.close()


def main():
    game = TicTacToeGame()
    game.get_board()

    current_player = 'X'

    running = True

    while running:

        print(f'Ход делает {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row > 2:
                    raise FieldIndexError

                col = int(input('Введите номер столбца: '))
                if col < 0 or col > 2:
                    raise FieldIndexError

                if game.board[row][col] != ' ':
                    raise CellOccupiedError

            except FieldIndexError:
                print()
                print(f'Значение должно быть'
                      f'положительным и меньше {game.a}')
                print('укажите верное значение')
                print()
                continue

            except CellOccupiedError:
                print()
                print('Вы не можете занять не пустую ячейку!')
                print('Введите новую ячейку!')
                print()
                continue

            except ValueError:
                print()
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения '
                      'для строки и столбца заново.')
                print()
                continue

            except Exception:
                print()
                print(f'Возникла ошибка {Exception}')
                print()
                continue

            else:
                break

        game.get(row, col, current_player)
        print('Ход сделан!')
        game.get_board()

        if game.check_win(current_player):
            print(f'Победил {current_player}.')
            save_result(f'Победил {current_player}')
            running = False

        elif game.game_over():
            print('Ничья!')
            save_result('Ничья!')
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()

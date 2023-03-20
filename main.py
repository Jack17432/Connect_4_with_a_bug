from board import Board


def main():
    board = Board((5, 4))

    while True:
        board.display_board()
        move_x, move_y = input(f"Player 1 make a move (format is 'row col')\n").split(" ")
        board.make_move("x", (int(move_x), int(move_y)))
        while None is board.make_move("o", (int(move_x), int(move_y))):
            move_x, move_y = input(f"invalid move someone is there(format is 'row col')\n").split(" ")

        is_over, player = board.is_game_over()
        if is_over:
            print(f"Game is over player {player} wins !!!!!!!!")
            break

        board.display_board()
        move_x, move_y = input(f"Player 2 make a move (format is 'row col')\n").split(" ")
        while None is board.make_move("o", (int(move_x), int(move_y))):
            move_x, move_y = input(f"invalid move someone is there(format is 'row col')\n").split(" ")

        is_over, player = board.is_game_over()
        if is_over:
            print(f"Game is over player {player} wins !!!!!!!!")
            break


if __name__ == "__main__":
    main()

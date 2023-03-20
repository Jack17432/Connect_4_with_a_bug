from typing import Optional


class Board:
    def __init__(self, size_of_board: (int, int) = (4, 4)):
        """
        Creates a game of Connect 4

        :param size_of_board: Length by width of board
        """
        self.size_of_board: (int, int) = size_of_board
        self.row = size_of_board[0]
        self.col = size_of_board[1]

        self.board = [["_"] * size_of_board[1]] * size_of_board[0]

    def make_move(self, player: str, position: (int, int)) -> Optional[int]:
        """
        Makes a move on the Connect 4 board for the given player at the specified position.
        Args:
            player: A string representing the player making the move.
            position: A tuple representing the (row, column) position on the board where the move is to be made.
        Returns:
            An optional integer representing the player's score, if the move results in a win, otherwise None.
        Raises:
            ValueError: If the position is outside the board boundaries, or if the player is not "x" or "o".
        """
        if position > self.size_of_board:
            raise ValueError("Play inside the self.board please")
        elif player not in ["x", "o"]:
            raise ValueError("Your not a real player!")

        if self.board[position[1]][position[0]] != "_":
            return None
        else:
            self.board[position[1]][position[0]] = player

    def count_points(self, player: str) -> (int, int):
        """
        Counts the number of points for the given player on the Connect 4 board.
        A player earns a point for each line of 4 tokens (horizontally, vertically, or diagonally) that they have.
        Args:
            player: A string representing the player whose points are to be counted.
        Returns:
            A tuple of integers representing the player's total points for horizontal lines and diagonal lines,
            respectively.
        """
        points = 0
        
        # Check horizontally
        for row in range(self.row):
            for col in range(self.col - 3):
                if self.board[row][col] == player and self.board[row][col + 1] == player \
                        and self.board[row][col + 2] == player and self.board[row][col + 3] == player:
                    points += 1

        # Check vertically
        for row in range(self.row - 3):
            for col in range(self.col):
                if self.board[row][col] == player and self.board[row + 1][col] == player \
                        and self.board[row + 2][col] == player and self.board[row + 3][col] == player:
                    points += 1

        # Check diagonally (down-right)
        for row in range(self.row - 3):
            for col in range(self.col - 3):
                if self.board[row][col] == player and self.board[row + 1][col + 1] == player \
                        and self.board[row + 2][col + 2] == player and self.board[row + 3][col + 3] == player:
                    points += 1

        # Check diagonally (down-left)
        for row in range(self.row - 3):
            for col in range(3, self.col):
                if self.board[row][col] == player and self.board[row + 1][col - 1] == player \
                        and self.board[row + 2][col - 2] == player and self.board[row + 3][col - 3] == player:
                    points += 1

        return points

    def display_board(self) -> None:
        """
        Prints the current state of the Connect 4 board and the number of points earned by each player.
        Displays the board as a grid of tokens, and calculates the points for each player using the count_points
        function.
        """
        print(f"----------------------------")
        for row in self.board:
            print(f"{row}")

        player_1_points = self.count_points("x")
        player_2_points = self.count_points("o")
        print(f"The points players have are:"
              f"player 1 = {player_1_points}, Player 2 = {player_2_points}")

    def is_game_over(self) -> (bool, str):
        """
        Checks if the Connect 4 game is over by determining if the board is full. If the game is over, it returns True
        along with the winner's token ("x" or "o") based on the points earned by each player. Otherwise, it returns
        False and an empty string.
        Returns:
        - A tuple containing a boolean value indicating if the game is over, and a string representing the winner's
        token.
        """
        num_of_col_without_null = 0

        for row in self.board:
            if "_" not in row:
                num_of_col_without_null += 1

        if num_of_col_without_null == self.col:
            return True, "x" if self.count_points("x") > self.count_points("o") else "o"
        else:
            return False, ""

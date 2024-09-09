import random
from time import sleep
import click
import numpy as np
import sys
from colorama import Fore, init
# import os
from tictactoe.player import Player
from tictactoe.board import Board
from tictactoe.coordinate import Coordinate

init(autoreset=True)


class TicTacToe:

    """TicTacToe game against computer
    """

    def __init__(self, n: int = 3) -> None:
        """Initializes game and creates board

        Arguments:
            n (int): size of nxn board
        """

        self.n = n
        self.board = self.create_board()

    def create_board(self) -> Board:

        """Creates Board object

        Returns:
            Board: board object
        """

        return Board(self.n)

    def parse_coordinate(self, data: str) -> Coordinate:
        """Parse coordinate string to tuple

        Arguments:
            data (str) coordinate as string to parse like 'x,y'
        Returns:
            Coordinate coordinate object with y and x members
        """

        x, y = map(
            lambda x: int(x)-1,
            data.strip().replace(" ", "").split(",")
            )
        return Coordinate(y, x)

    def set_coordinate(self, player: Player, coordinate: Coordinate) -> None:

        """Set given coordinate to board for given player

        Arguments:
            player (Player) player
            y (int) coordinate index for board rows
            x (int) coordinate index for board columns
        """

        self.board[coordinate] = player

    def print_win(self, player: Player) -> None:
        print(Fore.RED+f"Player {player} wins\n")

    def print_coordinate_error(self, coordinate: Coordinate) -> None:
        print(f"{coordinate.x+1},{coordinate.y+1} is not available")

    def print_game_header(self) -> None:
        print(
            Fore.RED+f"Player 0: {Player.PLAYER_0}\n"
            f"Player 1: {Player.PLAYER_1}\n\n"
            )

    def print_player_header(self, player: Player) -> None:
        print(Fore.RED+f"Player {player}")

    def print_screen(self, player: Player) -> None:
        """Updates screen

        Arguments:
            message (str) Message to print on screen
        """

        click.clear()

        self.print_game_header()

        if self.is_win(player):
            self.print_win(player)
            self.print_board()
            sys.exit(0)

        self.print_player_header(player)
        self.print_board()

    def get_random_move(self) -> Coordinate:

        """Wait 1 second and generate and returns random coordinate

        Returns:
            Coordinate: coordinate object with members y and x or None
        """

        sleep(1)

        movements = self.calc_possibilities()
        if not movements.size:
            return None
        y, x = random.choice(movements)

        return Coordinate(y, x)

    def move_player(
        self, player: Player, coordinate: Coordinate
                    ) -> None:

        """Moves player with given coordinate

        Arguments:
            player (Player) player to move
            coordinate (Coordinate) coordinate object with members x and y
        """
        self.set_coordinate(player, coordinate)

        self.print_screen(player)

    def run(self):
        """Starts game and loop
        """

        # self.print_screen(
        #     f"Player 0: {Player.PLAYER_0}\nPlayer 1: {Player.PLAYER_1}\n\n"
        #     )
        self.print_screen(Player.PLAYER_0)

        while True:
            try:

                data = input("Please enter coordinates: ")

                coordinate = self.parse_coordinate(data)

                if not self.is_available(coordinate):
                    self.print_coordinate_error(coordinate)
                    continue

                self.move_player(Player.PLAYER_0, coordinate)

                coordinate = self.get_random_move()

                if not coordinate:
                    sys.exit(0)

                self.move_player(Player.PLAYER_1, coordinate)

            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)
                sys.exit(-1)

    def calc_possibilities(self) -> np.ndarray:
        """
        Calculates possible locations

        Returns:
            numpy.ndarray: contains possible locations
        """
        return np.argwhere(self.board == Player.UNKNOWN)

    def print_board(self) -> None:
        """
        Prints current board
        """
        print(self.board)

    def is_available(self, coordinate: Coordinate) -> bool:
        """Check availability of that cell

        Arguments:
            y (int) coordinate index of board rows
            x (int) coordinate index of board columns

        Returns:
            bool: cell is available or not
        """
        if self.board[coordinate] == Player.UNKNOWN:
            return True  # check location is available
        return False

    def is_win(self, player: Player) -> bool:
        """Checks rows columns and diagonals to find player won or not

        Returns:
            bool: player wins or not
        """

        return self.board.check_complete(player)

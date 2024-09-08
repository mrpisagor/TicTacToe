import numpy as np
from tictactoe.player import Player
from tictactoe.coordinate import Coordinate
from colorama import Fore


class Board:
    def __init__(self, n: int) -> None:
        """Initialize numpy array to hold board data as nxn matrix

        Arguments:
            n (int) size of nxn board
        """
        self._arr = np.full((n, n), Player.UNKNOWN)

    def __getitem__(self, coordinate: Coordinate) -> Player:
        """Gets player on board from given coordinate fetch from 2D numpy array

        Arguments:
            coordinate (Coordinate) coordinate object with member x and y

        Returns:
            Player: current player on that coordinate
        """
        return self._arr[coordinate.y, coordinate.x]

    def __setitem__(self, coordinate: Coordinate, player: Player) -> None:
        """Sets player on board to given coordinate stores at 2D numpy array

        Arguments:
            coordinate (Coordinate) coordinate object with member x and y
            player (Player) current player to set
        """
        self._arr[coordinate.y, coordinate.x] = player

    def __eq__(self, player: Player) -> None:
        """Checks equality of player all board items stored on 2D numpy array

        Arguments:
            player (Player) current player to compare with board
        """
        return self._arr == player

    def __str__(self):
        """Give board a view

        Returns:
            str: board shows when printing like that
        """

        showing = Fore.RED
        showing += "\n  1 2 3\n"

        for i, row in enumerate(self._arr):
            showing += Fore.RED + str(i+1) + " " + Fore.BLUE
            showing += " ".join(
                map(lambda x: "-" if x == Player.UNKNOWN else str(x), row)
                )
            showing += "\n"

        return showing

    def check_complete_column(self, player: Player) -> bool:
        """Checks any column is completed with same player

        Arguments:
            player (Player) player to check

        Returns:
            bool: completed or not
        """
        # checks column complete
        return np.all(self._arr == player, axis=0).any()

    def check_complete_row(self, player: Player) -> bool:
        """Checks any row is completed with same player

        Arguments:
            player (Player) player to check

        Returns:
            bool: completed or not
        """
        # checks row complete
        return np.all(self._arr == player, axis=1).any()

    def check_complete_diag(self, player: Player) -> bool:
        """Checks diagonal is completed with same player

        Arguments:
            player (Player) player to check

        Returns:
            bool: completed or not
        """
        # checks diagonal complete
        return np.all(np.diag(self._arr) == player)

    def check_complete_rotdiag(self, player: Player) -> bool:
        """Checks other diagonal is completed with same player

        Arguments:
            player (Player) player to check

        Returns:
            bool: completed or not
        """
        # checks other diagonal complete
        return np.all(np.diag(np.rot90(self._arr)) == player)

    def check_complete(self, player: Player) -> bool:

        return any(
            [
                self.check_complete_column(player),
                self.check_complete_row(player),
                self.check_complete_diag(player),
                self.check_complete_rotdiag(player)
            ]
        )

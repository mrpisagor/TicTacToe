from enum import Enum


class Player(Enum):
    UNKNOWN = -1
    PLAYER_0 = 0
    PLAYER_1 = 1

    def __str__(self) -> str:
        return str(self.value)

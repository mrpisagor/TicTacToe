from dataclasses import dataclass


@dataclass
class Coordinate:
    y: int
    x: int

    def __init__(self, y, x):
        self.y = y
        self.x = x

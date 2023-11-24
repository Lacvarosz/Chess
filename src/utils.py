from typing import Self
from enum import Enum

class SideColor(Enum):
    WHITE = 0
    BLACK = 1

class bcolors():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class IllegalPosition(Exception):
    pass

class IllegalStringformat(Exception):
    pass

class Position():
    def __init__(self, x :int, y :int) -> None:
        if x < 0 or y < 0 or x > 7 or y > 7:
            raise IllegalPosition
        self.x = x
        self.y = y
    
    def __getitem__(self, x :int, y :int) -> None:
        self.x, self.y = x, y
    
    def __str__(self) -> str:
        return(f"({self.x}, {self.y})")
    
    def __add__(self, pos2 :Self) -> bool:
        return(self.x == pos2.x or self.y == pos2.y)
    
    def __mul__(self, pos2 :Self) -> bool:
        return(abs(self.x - pos2.x) == abs(self.y - pos2.y))
    
    def __eq__(self, __value: Self) -> bool:
        return (self.x == __value.x and self.y == __value.y)
    
    @staticmethod
    def str_to_pos(s :str) -> Self:
        c = "abcdefgh"
        r = "12345678"
        if len(s) != 2 or s[0] not in c or s[1] not in r:
            raise IllegalStringformat("A pos string must be a letter 'a-h' and a digit '1-8'")
        return Position(c.find(s[0]), 8 - int(s[1]))
    
    @staticmethod
    def str_to_x(s :str) -> int:
        c = "abcdefgh"
        if len(s) != 1 or s[0] not in c:
            raise IllegalStringformat("A pos string must be a letter 'a-h' and a digit '1-8'")
        return c.find(s)
    
    @staticmethod
    def str_to_y(s :str) -> int:
        r = "12345678"
        if len(s) != 2 or s[1] not in r:
            raise IllegalStringformat("A pos string must be a letter 'a-h' and a digit '1-8'")
        return 8 - int(s)
            
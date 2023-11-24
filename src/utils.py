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

class Position():
    def __init__(self, x :int, y :int) -> None:
        if x < 0 or y < 0 or x > 7 or y > 7:
            raise 
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
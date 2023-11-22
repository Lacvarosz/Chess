from enum import Enum
class Site(Enum):
    WHITE = 0
    BLACK = 1

class Figure():
    def __init__(self, x :int, y :int, color :Site) -> None:
        self.x = x
        self.y = y
        self.color = color
    
    def set_pos(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
    
    def __getitem__(self, x:int, y :int) -> None:
        self.set_pos(x, y)

class Pawn(Figure):
    def __init__(self, x: int, y: int, color: Site) -> None:
        super().__init__(x, y, color)
        self.base_step_in_previous_round = False
        
    def __getitem__(self, x: int, y: int) -> bool:
        return self.simple_step(x, y)
    
    def simple_step(self, x :int, y:int) -> bool:
        if self.color == Site.WHITE:
            l = x == self.x and y + 1 == self.y
            if l:
                super()[x, y]
        else:
            l = y - 1 == self.y and x == self.x
            if l:
                super()[x, y]
        return(l)
    
    def takes(self, x :int, y :int) ->bool:
        if self.color == Site.WHITE:
            l = abs(x - self.x) == 1 and y + 1 == self.y
            if l:
                super()[x, y]
        else:
            l = abs(x - self.x) == 1 and y - 1 == self.y
            if l:
                super()[x, y]
        return(l)
    
    def base_step(self, x :int, y :int) ->bool:
        if self.color == Site.WHITE:
            l = x == self.x and y + 2 == self.y and y == 6
            if l:
                super()[x, y]
        else:
            l = y - 2 == self.y and x == self.x and y == 1
            if l:
                super()[x, y]
        if l:
            self.base_step_in_previous_round = True
        return(l)
    
    def en_passant(self, x :int, y :int) -> bool:
        return(self.takes(x, y))
    
    def next_round(self):
        self.base_step_in_previous_round = False

class King(Figure):
    def __init__(self, x: int, y: int, color: Site) -> None:
        super().__init__(x, y, color)
        self.didnt_move = True
    
    def __getitem__(self, x: int, y: int) -> bool:
        return(self.step(x, y))
    
    def step(self, x :int, y :int) -> bool:
        l = max(abs(self.x -x), (self.y - y)) == 1
        if l:
            super()[x, y]
            self.didnt_move = False
        return(l)
    
    def castling(self, x :int, y :int) -> bool:
        l = self.didnt_move and abs(self.x - x) == 2 and self.y == y
        if l:
            self.didnt_move = False
            super()[x, y]
        return(l)

class Queen(Figure):
    def __init__(self, x: int, y: int, color: Site) -> None:
        super().__init__(x, y, color)
    
    def __getitem__(self, x: int, y: int) -> bool:
        return self.step(x, y)
    
    def step(self, x :int, y :int) -> bool:
        l = (x == self.x or y == self.y) or (abs(self.x - x) == abs(self.y - y))
        if l:
            super()[x, y]
        return(l)

class Rook(Figure):
    def __init__(self, x: int, y: int, color: Site) -> None:
        super().__init__(x, y, color)
    
    def __getitem__(self, x: int, y: int) -> bool:
        return self.step(x, y)
    
    def step(self, x :int, y :int) -> bool:
        l = x == self.x or y == self.y
        if l:
            super()[x, y]
        return(l)
    
class Bishop(Figure):
    def __init__(self, x: int, y: int, color: Site) -> None:
        super().__init__(x, y, color)
    
    def __getitem__(self, x: int, y: int) -> bool:
        return self.step(x, y)
    
    def step(self, x :int, y :int) -> bool:
        l = (abs(self.x - x) == abs(self.y - y))
        if l:
            super()[x, y]
        return(l)
    
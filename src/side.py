from figure import *
from typing import Self

class Side():
    def __init__(self, color :SideColor) -> None:
        self.figures = []
        self.color = color
    
    def __getitem__(self, i :int) -> Figure:
        return(self.figures[i])
    
    def __setitem__(self, i :int, new_value :Figure) -> None:
        self.figures[i] = new_value
    
    def __iter__(self) -> Self:
        self.ind = 0
        return self
    
    def __next__(self) -> Figure:
        if self.ind < len(self.figures):
            ret = self.figures[self.ind]
            self.ind += 1
            return(ret)
        else:
            raise StopIteration
    
    def __add__(self, side2 :Self) -> list[Figure]:
        return(self.figures + side2.figures)
    
    def __delitem__(self, pos :Position) -> None:
        k = 0
        for i in range(len(self.figures)):
            if self.figures[i - k].pos == pos:
                del self.figures[i - k]
                k += 1

    def get_by_type(self, f :type) -> list[Figure]:
        ret = []
        for i in self:
            if isinstance(i, f):
                ret.append(i)
        return(ret)
        
    def starting_stand(self):
        if self.color == SideColor.WHITE:
            for i in range(8):
                self.figures.append(Pawn(Position(i,6),self.color))
            self.figures.append(Rook(Position(0,7),self.color))
            self.figures.append(Rook(Position(7,7),self.color))
            self.figures.append(Knight(Position(1,7),self.color))
            self.figures.append(Knight(Position(6,7),self.color))
            self.figures.append(Bishop(Position(2,7),self.color))
            self.figures.append(Bishop(Position(5,7),self.color))
            self.figures.append(King(Position(4,7),self.color))
            self.figures.append(Queen(Position(3,7),self.color))
        else:
            for i in range(8):
                self.figures.append(Pawn(Position(i,1),self.color))
            self.figures.append(Rook(Position(0,0),self.color))
            self.figures.append(Rook(Position(7,0),self.color))
            self.figures.append(Knight(Position(1,0),self.color))
            self.figures.append(Knight(Position(6,0),self.color))
            self.figures.append(Bishop(Position(2,0),self.color))
            self.figures.append(Bishop(Position(5,0),self.color))
            self.figures.append(King(Position(4,0),self.color))
            self.figures.append(Queen(Position(3,0),self.color))

if __name__ == "__main__":
    white = Side(SideColor.WHITE)
    white.starting_stand()
    del white[Position(0, 7)]
    for f in white:
        print(f, f.pos)
from side import *

class Board():
    def __init__(self) -> None:
        self.sides = {SideColor.WHITE : Side(SideColor.WHITE), SideColor.BLACK :Side(SideColor.BLACK)}
        self.sides[SideColor.WHITE].starting_stand()
        self.sides[SideColor.BLACK].starting_stand()
        self.refresh_map()
    
    def __getitem__(self, pos :Position) -> Figure:
        return (self.board[pos.y][pos.x])
    
    def __setitem__(self, pos :Position, new_value :Figure) -> None:
        self.board[pos.y][pos.x] = new_value
    
    def __delitem__(self, pos:Position) -> None:
        del self.sides[self[pos].color][pos]
    
    def __str__(self) -> str:
        ret = "+" + "---+"*8 + "\n"
        for i in range(8):
            ret += "|"
            for j in range(8):
                if not self.board[i][j] is None:
                    ret += " " + str(self.board[i][j]) + " |"
                else:
                    ret += "   |"
            ret += " " + str(8-i) + "\n" + "+" + "---+"*8 + "\n"
        ret += " "
        for j in list("abcdefgh"):
            ret += f" {j}  "
        return(ret)
    
    def __iter__(self) -> Self:
        self.iter = iter(self.sides[SideColor.WHITE] + self.sides[SideColor.BLACK])
        return self
    
    def __next__(self) -> Figure:
        return (self.iter.__next__())
    
    def line_is_clear(self, p1 :Position, p2 :Position) -> bool:
        #felfelé
        if p1.y < p2.y and p1.x == p2.x:
            for i in range(p2.y-1, p1.y, -1):
                if self[Position(p1.x, i)] is not None:
                    return False
        #lefelé
        elif p1.y > p2.y and p1.x == p2.x:
            for i in range(p2.y+1, p1.y, 1):
                if self[Position(p1.x, i)] is not None:
                    return False
        #jobbra
        elif p1.y == p2.y and p1.x < p2.x:
            for i in range( p2.x-1, p1.x, -1):
                if self[Position(i, p1.y)] is not None:
                    return False
        #balra
        elif p1.y == p2.y and p1.x > p2.x:
            for i in range( p2.x+1, p1.x, 1):
                if self[Position(i, p1.y)] is not None:
                    return False
        return True
            
    def diag_is_clear(self, p1 :Position, p2 :Position) -> bool:
        #jobbra fel
        if p1.y > p2.y and p1.x < p2.x:
            for i in range(1, p1.y - p2.y, 1):
                if self[Position(p1.x + i, p1.y - i)] is not None:
                    return False
        #jobbra le
        elif p1.y < p2.y and p1.x < p2.x:
            for i in range(1, p2.y - p1.y, 1):
                if self[Position(p1.x + i, p1.y + i)] is not None:
                    return False
        #balra fel
        elif p1.y > p2.y and p1.x > p2.x:
            for i in range(1, p1.y - p2.y, 1):
                if self[Position(p1.x - i, p1.y - i)] is not None:
                    return False
        #balra le
        elif p1.y < p2.y and p1.x > p2.x:
            for i in range(1, p2.y - p1.y, 1):
                if self[Position(p1.x - i, p1.y + i)] is not None:
                    return False
        return True

    def castling_is_clear(self, side :SideColor, inner_fields :list[Position]) -> bool:
        for i in inner_fields:
            for f in self.sides[side]:
                if not self.can_step(f.pos, i, side):
                    print("A vonalban ütés lenne", f, f.pos)
                    return False
        return True
    
    def refresh_map(self):
        self.board = [[None]*8 for i in range(8)]
        
        for k in self.sides:
            for f in self.sides[k]:
                self[f.pos] = f
    
    def can_step(self, w :Position, t :Position, color :SideColor) -> bool:
        if self[w] is None:
            print("Ez nem bábu")
            return False
        figure = self[w]
        #Figure is owned by enemy
        if figure.color != color:
            return False
        #You can't step the place of your other figure
        if self[t] is not None and self[t].color == figure.color:
            print("ki akarom ütni a saját bábumat")
            return False
        #linear movement
        if w + t and not self.line_is_clear(w, t):
            print("Vonalban lépek, de nem léphetek")
            return False
        if w * t and not self.diag_is_clear(w, t):
            print("Átlóban lépek, de nem léphetek")
            return False
        #capture
        if self[t] is not None:
            print("Ütés")
            if isinstance(figure, Pawn):
                return figure.can_takes(t)
        # elif isinstance(figure, Pawn) and abs(w.x - t.x) == abs(w.y - t.y):
        #     print("A gyalog csak ütni tud átlósan")
        #     return False
        #castling
        if isinstance(figure, King) and abs(t.x - w.x) == 2 and figure.didnt_move:
            if t.x > w.x:
                if isinstance(self[Position(7, t.y)], Rook) and self[Position(7, t.y)].didnt_move and self.line_is_clear(w, Position(7, t.y)) and self.castling_is_clear(SideColor.BLACK if figure.color == SideColor.WHITE else SideColor.WHITE, [Position(5, t.y), Position(6, t.y)]):
                    if figure.can_castling(t):
                        return True
                    
            elif t.x < w.x:
                if isinstance(self[Position(0, t.y)], Rook) and self[Position(0, t.y)].didnt_move and self.line_is_clear(w, Position(0, t.y)) and self.castling_is_clear(SideColor.BLACK if figure.color == SideColor.WHITE else SideColor.WHITE, [Position(3, t.y), Position(2, t.y)], Position(1, t.y)):
                    if figure.can_castling(t):
                        return True
            return False
        #Pawn dubble step
        if isinstance(figure, Pawn) and figure.can_base_step(t):
            return True
        print("Egyszerü lépés")
        return figure.can_step(t)
    
    def step(self, w :Position, t :Position, color :SideColor) -> bool:
        if self[w] is None:
            print("Ez nem bábu")
            return False
        figure = self[w]
        #Figure is owned by enemy
        if figure.color != color:
            return False
        #You can't step the place of your other figure
        if self[t] is not None and self[t].color == figure.color:
            print("ki akarom ütni a saját bábumat")
            return False
        #linear movement
        if w + t and not self.line_is_clear(w, t):
            print("Vonalban lépek, de nem léphetek")
            return False
        if w * t and not self.diag_is_clear(w, t):
            print("Átlóban lépek, de nem léphetek")
            return False
        if self[t] is not None:
            print("Ütés")
            if isinstance(figure, Pawn) and w.x == t.x:
                print("A gyalog nem tud előre ütni")
                return False
            if figure[t]:
                del self[t]
                print("sikeres ütés")
                return True
            return False
        if isinstance(figure, Pawn) and abs(w.x - t.x) == abs(w.y - t.y):
            print("A gyalog csak ütni tud átlósan")
            return False
        #castling
        if isinstance(figure, King) and abs(t.x - w.x) == 2 and figure.didnt_move:
            if t.x > w.x:
                if isinstance(self[Position(7, t.y)], Rook) and self[Position(7, t.y)].didnt_move and self.line_is_clear(w, Position(7, t.y)) and self.castling_is_clear(SideColor.BLACK if figure.color == SideColor.WHITE else SideColor.WHITE, [Position(5, t.y), Position(6, t.y)]):
                    if figure.can_castling(t):
                        figure.castling(t)
                        self[Position(7, t.y)].castling(Position(t.x-1, t.y))
                        return True
                    
            elif t.x < w.x:
                if isinstance(self[Position(0, t.y)], Rook) and self[Position(0, t.y)].didnt_move and self.line_is_clear(w, Position(0, t.y)) and self.castling_is_clear(SideColor.BLACK if figure.color == SideColor.WHITE else SideColor.WHITE, [Position(3, t.y), Position(2, t.y), Position(1, t.y)]):
                    if figure.can_castling(t):
                        figure.castling(t)
                        self[Position(0, t.y)].castling(Position(t.x+1, t.y))
                        return True
            return False        
            
        if figure[t]:
            print("egyszerű lépés")
            return True
        print("Érvénytelen lépés")
        return False
    
    def is_check(self, side :SideColor) -> bool:
        op_side = SideColor.WHITE if side == SideColor.BLACK else SideColor.BLACK
        pos = self.sides[side].get_by_type(King)[0].pos
        for i in self.sides[op_side]:
            if self.can_step(i.pos, pos, op_side):
                return True
        return False
                
            

if __name__ == "__main__":
    b = Board()
    print(b)
    if b.step(Position(6, 6), Position(6, 4), SideColor.WHITE):
        b.refresh_map()
        print(b)
    if b.step(Position(5, 7), Position(7, 5), SideColor.WHITE):
        b.refresh_map()
        print(b)
    if b.step(Position(6, 7), Position(5, 5), SideColor.WHITE):
        b.refresh_map()
        print(b)
    if b.step(Position(5, 5), Position(7, 4), SideColor.WHITE):
        b.refresh_map()
        print(b)
    if b.step(Position(4, 7), Position(5, 5), SideColor.WHITE):
        b.refresh_map()
        print(b)
    if b.step(Position(4, 7), Position(0, 3), SideColor.WHITE):
        b.refresh_map()
        print(b)
    if b.step(Position(4, 7), Position(6, 7), SideColor.WHITE):
        b.refresh_map()
        print(b)
    if b.step(Position(5, 6), Position(5, 5), SideColor.WHITE):
        b.refresh_map()
        print(b)
    if b.step(Position(6, 7), Position(0, 1), SideColor.WHITE):
        b.refresh_map()
        print(b)
    if b.step(Position(0, 1), Position(1, 0), SideColor.BLACK):
        b.refresh_map()
        print(b)
    if b.step(Position(1, 0), Position(6, 5), SideColor.BLACK):
        b.refresh_map()
        print(b)
    if b.step(Position(2, 1), Position(2, 3), SideColor.BLACK):
        b.refresh_map()
        print(b)
    if b.step(Position(2, 3), Position(2, 4), SideColor.BLACK):
        b.refresh_map()
        print(b)
    if b.step(Position(2, 4), Position(2, 5), SideColor.BLACK):
        b.refresh_map()
        print(b)
    if b.step(Position(2, 5), Position(2, 6), SideColor.BLACK):
        b.refresh_map()
        print(b)
    if b.step(Position(2, 5), Position(3, 6), SideColor.BLACK):
        b.refresh_map()
        print(b)
    if b.step(Position(3, 0), Position(2, 1), SideColor.BLACK):
        b.refresh_map()
        print(b)
    if b.step(Position(3, 6), Position(4, 7), SideColor.WHITE):
        b.refresh_map()
        print(b)
    if b.step(Position(3, 7), Position(5, 7), SideColor.WHITE):
        b.refresh_map()
        print(b)         
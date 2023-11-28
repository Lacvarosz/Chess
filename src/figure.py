from utils import *



class Figure():
    def __init__(self, pos :Position, color :SideColor) -> None:
        self.pos = pos
        self.color = color
    
    def set_pos(self, pos :Position) -> None:
        self.pos = pos
    
    def __getitem__(self, pos :Position) -> None:
        self.set_pos(pos)
    
    def __str__(self) -> str:
        return (f"{bcolors.OKGREEN if self.color == SideColor.WHITE else bcolors.OKBLUE}ff{bcolors.ENDC}")

class Pawn(Figure):
    def __init__(self, pos :Position, color: SideColor) -> None:
        super().__init__(pos, color)
        self.base_step_in_previous_round = False
        
    def __getitem__(self, pos :Position) -> bool:
        if abs(self.pos.y - pos.y) == 2 and self.can_base_step(pos):
            print("Első dupla")
            self.base_step(pos)
            return True
        if self.can_takes(pos) or self.can_step(pos):
            print("Sima lépés")
            self.set_pos(pos)
            return True
        return False
    
    def __str__(self) -> str:
        return (f"{bcolors.OKGREEN if self.color == SideColor.WHITE else bcolors.OKBLUE}P{bcolors.ENDC}")
    
    def can_step(self, pos: Position) -> bool:
        if self.color == SideColor.WHITE:
            l = pos.x == self.pos.x and pos.y + 1 == self.pos.y
        else:
            l = pos.y - 1 == self.pos.y and pos.x == self.pos.x
        return(l)
        
    def can_takes(self, pos : Position) -> bool:
        if self.color == SideColor.WHITE:
            l = abs(pos.x - self.pos.x) == 1 and pos.y + 1 == self.pos.y
        else:
            l = abs(pos.x - self.pos.x) == 1 and pos.y - 1 == self.pos.y
        return(l)
    
    def can_base_step(self, pos :Position) -> bool:
        if self.color == SideColor.WHITE:
            l = pos.x == self.pos.x and pos.y + 2 == self.pos.y and self.pos.y == 6
        else:
            l = pos.y - 2 == self.pos.y and pos.x == self.pos.x and self.pos.y == 1
        return(l)
    
    def base_step(self, pos :Position) -> None:
        self.set_pos(pos)
        self.base_step_in_previous_round = True
    
    def en_passant(self, pos :Position) -> bool:
        return(self.takes(pos))
    
    def next_round(self):
        self.base_step_in_previous_round = False

class King(Figure):
    def __init__(self, pos :Position, color: SideColor) -> None:
        super().__init__(pos, color)
        self.didnt_move = True
    
    def __getitem__(self, pos :Position) -> bool:
        if self.can_step(pos):
            self.step(pos)
            return True
        return False
    
    def __str__(self) -> str:
        return (f"{bcolors.OKGREEN if self.color == SideColor.WHITE else bcolors.OKBLUE}K{bcolors.ENDC}")
    
    def can_step(self, pos :Position) -> bool:
        return(max(abs(self.pos.x - pos.x), abs(self.pos.y - pos.y)) == 1)
        
    
    def step(self, pos :Position) -> None:
        self.set_pos(pos)
        self.didnt_move = False
    
    def can_castling(self, pos :Position) ->bool:
        return(self.didnt_move and abs(self.pos.x - pos.x) == 2 and self.pos.y == pos.y)
    
    def castling(self, pos :Position) -> None:
        self.didnt_move = False
        self.set_pos(pos)

class Queen(Figure):
    def __init__(self, pos :Position, color: SideColor) -> None:
        super().__init__(pos, color)
    
    def __getitem__(self, pos :Position) -> bool:
        if self.can_step(pos):
            self.set_pos(pos)
            return True
        return False
    
    def __str__(self) -> str:
        return (f"{bcolors.OKGREEN if self.color == SideColor.WHITE else bcolors.OKBLUE}Q{bcolors.ENDC}")
    
    def can_step(self, pos :Position) -> bool:
        return((pos.x == self.pos.x or pos.y == self.pos.y) or (abs(self.pos.x - pos.x) == abs(self.pos.y - pos.y)))

class Rook(Figure):
    def __init__(self, pos :Position, color: SideColor) -> None:
        super().__init__(pos, color)
        self.didnt_move = True
    
    def __getitem__(self, pos :Position) -> bool:
        if self.can_step(pos):
            self.set_pos(pos)
            self.didnt_move = False
            return True
        return False
    
    def __str__(self) -> str:
        return (f"{bcolors.OKGREEN if self.color == SideColor.WHITE else bcolors.OKBLUE}R{bcolors.ENDC}")
    
    def can_step(self, pos :Position) -> bool:
        return(pos.x == self.pos.x or pos.y == self.pos.y)
    
    def castling(self, pos :Position) -> bool:
        self.set_pos(pos)
        self.didnt_move = False
    
class Bishop(Figure):
    def __init__(self, pos :Position, color: SideColor) -> None:
        super().__init__(pos, color)
    
    def __getitem__(self, pos :Position) -> bool:
        if self.can_step(pos):
            self.set_pos(pos)
            return True
        return False
    
    def __str__(self) -> str:
        return (f"{bcolors.OKGREEN if self.color == SideColor.WHITE else bcolors.OKBLUE}B{bcolors.ENDC}")
    
    def can_step(self, pos :Position) -> bool:
        return(abs(self.pos.x - pos.x) == abs(self.pos.y - pos.y))

class Knight(Figure):
    def __init__(self, pos :Position, color: SideColor) -> None:
        super().__init__(pos, color)
    
    def __getitem__(self, pos :Position) -> bool:
        if self.can_step(pos):
            self.set_pos(pos)
            return True
        return False
    
    def __str__(self) -> str:
        return (f"{bcolors.OKGREEN if self.color == SideColor.WHITE else bcolors.OKBLUE}N{bcolors.ENDC}")
    
    def can_step(self, pos :Position) -> bool:
        return ((abs(self.pos.x - pos.x) == 2 and abs(self.pos.y - pos.y) == 1) or (abs(self.pos.x - pos.x) == 1 and abs(self.pos.y - pos.y) == 2))
from board import *

b = Board()
a = input()
step_counter = 0
while a:
    side = SideColor.BLACK if step_counter % 2 else SideColor.WHITE
    w = None
    t = None
    if a == "o-o":
        for f in b.sides[side]:
            if isinstance(f, King):
                w = f.pos
                break
        t = Position(7, w.y)
    elif a == "o-o-o":
        for f in b.sides[side]:
            if isinstance(f, King):
                w = f.pos
                break
        t = Position(7, w.y)
    a = input()
from board import *

types = {
    "N" : Knight,
    "K" : King,
    "B" : Bishop,
    "R" : Rook,
    "Q" : Queen,
    "a" : Pawn, "b" : Pawn, "c" : Pawn, "d" : Pawn, "e" : Pawn, "f" : Pawn, "g" : Pawn, "h" : Pawn
}

b = Board()
print(b)
a = input()
step_counter = 0
while a:
    side = SideColor.BLACK if step_counter % 2 else SideColor.WHITE
    l = True
    w = None
    t = None
    if a == "o-o":
        for f in b.sides[side].get_by_type(King):
            w = f.pos
        t = Position(w.x+2, w.y)
    elif a == "o-o-o":
        for f in b.sides[side].get_by_type(King):
            w = f.pos
        t = Position(w.x-2, w.y)
    else:
        if types[a[0]] is Pawn:
            if len(a) == 3:
                try:
                    for f in b.sides[side].get_by_type(Pawn):
                        if Position.str_to_x(a[0]) == f.pos.x and b.can_step(f.pos, Position.str_to_pos(a[1:]), side):
                            w = f.pos
                            t = Position.str_to_pos(a[1:])
                except IllegalStringformat:
                    try:
                        for f in b.sides[side].get_by_type(Pawn):
                            if Position.str_to_y(a[0]) == f.pos.y and b.can_step(f.pos, Position.str_to_pos(a[1:]), side):
                                w = f.pos
                                t = Position.str_to_pos(a[1:])
                    except IllegalStringformat:
                        print("invalid input")
                        l = False
            elif len(a) == 2:
                try:
                    for f in b.sides[side].get_by_type(Pawn):
                        if b.can_step(f.pos, Position.str_to_pos(a), side):
                            w = f.pos
                            t = Position.str_to_pos(a)
                            print("OK")
                except IllegalStringformat:
                    print("Invalid input")
                    l = False
            else:
                print("invalid input")
                l = False
        else:
            if len(a) == 3:
                try:
                    for f in b.sides[side].get_by_type(types[a[0]]):
                        if b.can_step(f.pos, Position.str_to_pos(a[1:]), side):
                            w = f.pos
                            t = Position.str_to_pos(a[1:])
                except IllegalStringformat:
                    print("invalid input")
                    l = False
            elif len(a) == 4:
                try:
                    for f in b.sides[side].get_by_type(types(a[0])):
                        if Position.str_to_x(a[1]) == f.pos.x and b.can_step(f.pos, Position.str_to_pos(a[2:]), side):
                            w = f.pos
                            t = Position.str_to_pos(a[2:])
                except IllegalStringformat:
                    try:
                        for f in b.sides[side].get_by_type(types(a[0])):
                            if Position.str_to_y(a[1]) == f.pos.y and b.can_step(f.pos, Position.str_to_pos(a[2:]), side):
                                w = f.pos
                                t = Position.str_to_pos(a[2:])
                    except IllegalStringformat:
                        print("invalid input")
                        l = False
    if l and w is not None and b.can_step(w,t,side):
        b.step(w, t, side)
        step_counter += 1
        print(b)
    else:
        print("Hibás bemenet")
    a = input()
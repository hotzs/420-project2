from tile import tile
from solver import *
from three_board import three_board
from overlapping import overlapping
from triple_boards import *


def init_dict(board,dictionary):
    filled = 0
    for key in board:
        dictionary[key].set_num(board[key])
        if board[key] != 0:
            filled +=1
    percent_filled = filled/(19*9)
    return percent_filled
def test_base():
    test_board1 = {
        "a2" : 6,
        "a3" : 1,
        "a4" : 8,
        "a9" : 7,
        "b2" : 8,
        "b3" : 9,
        "b4" : 2,
        "b6" : 5,
        "b8" : 4,
        "c5" : 4,
        "c7" : 9,
        "c9" : 3,
        "d1" : 2,
        "d4" : 1,
        "d5" : 6,
        "d7" : 3,
        "e1" : 6,
        "e2" : 7,
        "e8" : 5,
        "e9" : 1,
        "f3" : 4,
        "f5" : 2,
        "f6" : 3,
        "f9" : 8,
        "g1" : 7,
        "g3" : 5,
        "g5" : 9,
        "h2" : 9,
        "h4" : 4,
        "h6" : 2,
        "h7" : 7,
        "h8" : 3,
        "i1" : 1,
        "i6" : 8,
        "i7" : 4,
        "i8" : 6
    }
    test_board2 = {
        #"a1" : 1,
        "a2" : 2,
        "a3" :3 ,
        #"a4" :4 ,
        "a5" :5 ,
        "a6" :6,
        "a7" :7 ,
        #"a8" :8,
        "a9" :9,
        "b1" : 4,
        "b2" :5 ,
        #"b3" :6,
        "b4" :7,
        "b5" :8,
        "b6" :9,
        #"b7" :1,
        "b8" :2,
        "b9" :3,
        "c1" :7,
        "c2" :8,
        "c3" :9,
        #"c4" :1,
        "c5" :2,
        "c6" :3,
        "c7" :4,
        "c8" :5,
        "c9" :6,
        "d1" :2,
        "d2" :3,
        #"d3" :1,
        "d4" :5,
        "d5" :6,
        "d6" :4,
        #"d7" :8,
        "d8" :9,
        "d9" :7,
        "e1" :5,
        "e2" :6,
        "e3" :4,
        "e4" :8,
        #"e5" :9,
        "e6" :7,
        "e7" :2,
        "e8" :3,
        "e9" :1,
        "f1" :8,
        "f2" :9,
        #"f3" :7,
        "f4" :2,
        "f5" :3,
        "f6" :1,
        "f7" :5,
        "f8" :6,
        "f9" :4,
        "g1" :3,
        #"g2" :1,
        "g3" :2,
        "g4" :6,
        "g5" :4,
        "g6" :5,
        "g7" :9,
        "g8" :7,
        "g9" :8,
        #"h1" :6,
        "h2" :4,
        "h3" :5,
        "h4" :9,
        #"h5" :7,
        "h6" :8,
        "h7" :3,
        "h8" :1,
        "h9" :2,
        #"i1" :9,
        "i2" :7,
        "i3" :8,
        "i4" :3,
        #"i5" :1,
        "i6" :2,
        "i7" :6,
        "i8" :4,
        "i9" :5
    }
    board = three_board()
    #init_dict(triple_board2,board.board_dict)
    #board.print_board()
    #doneboard=CSP_Solver(board,True, True, True, True)
    #doneboard.print_board()
    oboard = overlapping() 
    init_dict(triple_board10 ,oboard.board_dict)
    oboard.print_board()
    for key in oboard.board_dict:
        print(key," ",oboard.board_dict[key].get_constraints())
    doneboard=CSP_Solver(oboard,True, True, True, True)
    doneboard.print_board()
    print(doneboard.num_calls)

test_base()
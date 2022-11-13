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
    open = (19*9)-filled
    return open
def test_base():
    
    board = three_board()
    #init_dict(triple_board2,board.board_dict)
    #board.print_board()
    #doneboard=CSP_Solver(board,True, True, True, True)
    #doneboard.print_board()
    oboard = overlapping() 
    # init_dict(triple_board9 ,oboard.board_dict)
    # oboard.print_board()
    print("open ",init_dict(triple_board10 ,oboard.board_dict))
    oboard.print_board()
    for key in oboard.board_dict:
        print(key," ",oboard.board_dict[key].get_constraints())
    doneboard=CSP_Solver(oboard,True, True, True, True)
    doneboard.print_board()
    print(doneboard.num_calls)

test_base()
from tile import tile
from solver import *
from three_board import three_board



def init_dict(board,dictionary):
    for key in board:
        dictionary[key].set_num(board[key])
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
    board = three_board()
    init_dict(test_board1,board.board_dict)
    board.print_board()
    doneboard=backtrack(board,0)
    doneboard.print_board()
    # for i in range(1,10):
    #         o_str = ""
    #         for j in ["a","b","c","d","e","f","g","h","i"]:
    #             key = j + str(i)
    #             o_str+=str(doneboard[key].get_num())
    #             o_str += " "
    #         print(o_str)


test_base()
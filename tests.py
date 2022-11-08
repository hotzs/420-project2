from tile import tile
from solver import *
from three_board import three_board
from overlapping import overlapping


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
    test_board3 = {
        "a11" : 6, "a21" : 1, "a31" : 3, "a41" : 8, "a51" : 5, "a61" : 4,"a71" : 2,"a81" : 9,"a91" : 7,
        "b11" : 9,"b21" : 8,"b31" : 4,"b41" : 7, "b51" : 6, "b61" : 2, "b71" : 3, "b91" : 1,
        "c21" : 2,"c61" : 3,"c81" : 4,"c91" : 6,
        "d11" : 5,"d21" : 9,"d31" : 6,"d41" : 4,"d51" : 3,"d61" : 8,
        "e11" : 4,"e21" : 3,"e31" : 1,"e41" : 5,"e51" : 2,"e71" : 9, "e81" : 6, "e91" : 8,
        "f21" : 7, "f31" : 8, "f51" : 1, "f71" : 4, "f91" : 5,
        "g11" : 1, "g21" : 4, "g41" : 9, "g51" : 7, "g61" : 6,"g71" : 5,"g81" : 8,
        "h11" : 3, "h21" : 6, "h31" : 9, "h41" : 2, "h51" : 8, "h61" : 5,"h81" : 1,
        "i21" : 5, "i31" : 7,  "a51" : 4, "a61" : 1,"a71" : 6,"a91" : 9,
        "h22" : 4, "i12" : 6,
        "g42" : 7, "h52" : 5, "i42" : 3,
        "a92" : 7, "b82":8, "c72":4,
        "d92" : 9, "e82" : 1,
        "g72" : 3, "h82" : 2, "i92":8,
        "a93" : 1 , "b83": 3, "c73":7,
        "d93" : 2, "e83": 8, "f93": 7,
        "g33" : 9, "h23" : 6, "i13" : 1,
        "h53" : 5, "i43" : 9, "i63" : 2,
        "g73" : 1, "h83" : 9, "i93" : 4



    }
    board = three_board()
    init_dict(test_board1,board.board_dict)
    #board.print_board()
    #doneboard=CSP_Solver(board,True, True, True, True)
    #doneboard.print_board()
    oboard = overlapping()
    init_dict(test_board3,oboard.board_dict)
    oboard.print_board
    doneboard=CSP_Solver(oboard,True, True, True, True)
    doneboard.print_board()


test_base()
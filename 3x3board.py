from tile import tile
class three_board:
    def __init__(self):
        board_dict = {

        }

        for i in range(1,10):
            for j in range(1,10):
                temp_name = ""
                temp_back = ""
                temp_front = ""
                if i == 1:
                    temp_name +="a"
                    temp_back += "none"
                    temp_front += "b"
                elif i == 2:
                    temp_name +="b"
                    temp_back += "a"
                    temp_front += "c"
                elif i == 3:
                    temp_name +="c"
                    temp_back += "b"
                    temp_front += "d"
                elif i == 4:
                    temp_name +="d"
                    temp_back += "c"
                    temp_front += "e"
                elif i == 5:
                    temp_name +="e"
                    temp_back += "d"
                    temp_front += "f"
                elif i == 6:
                    temp_name +="f"
                    temp_back += "e"
                    temp_front += "g"
                elif i == 7:
                    temp_name +="g"
                    temp_back += "f"
                    temp_front += "h"
                elif i == 8:
                    temp_name +="h"
                    temp_back += "g"
                    temp_front += "i"
                elif i == 9:
                    temp_name +="i"
                    temp_back += "h"
                    temp_front += "none"
                letter = temp_name
                number = j
                temp_name += str(j)
                board_dict[temp_name] = tile(0,temp_name)
                if (letter == "a" or letter == "b" or letter == "c") and (number == 1 or number == 2 or number == 3):
                    board_dict[temp_name].set_family(1)
                elif (letter == "d" or letter == "e" or letter == "f") and (number == 1 or number == 2 or number == 3):
                    board_dict[temp_name].set_family(2)
                elif (letter == "g" or letter == "h" or letter == "i") and (number == 1 or number == 2 or number == 3):
                    board_dict[temp_name].set_family(3)
                elif (letter == "a" or letter == "b" or letter == "c") and (number == 4 or number == 5 or number == 6):
                    board_dict[temp_name].set_family(4)
                elif (letter == "d" or letter == "e" or letter == "f") and (number == 4 or number == 5 or number == 6):
                    board_dict[temp_name].set_family(5)
                elif (letter == "g" or letter == "h" or letter == "i") and (number == 4 or number == 5 or number == 6):
                    board_dict[temp_name].set_family(6)
                elif (letter == "a" or letter == "b" or letter == "c") and (number == 7 or number == 8 or number == 9):
                    board_dict[temp_name].set_family(7)
                elif (letter == "d" or letter == "e" or letter == "f") and (number == 7 or number == 8 or number == 9):
                    board_dict[temp_name].set_family(8)
                elif (letter == "g" or letter == "h" or letter == "i") and (number == 7 or number == 8 or number == 9):
                    board_dict[temp_name].set_family(9)
                

                #add column constraints
                for k in range (1,10):
                    temp_add = letter
                    if k!=i:
                        temp_add += str(k)
                        board_dict[temp_name].add_constraint(temp_add)
                #add row constraints
                for k in range (1,10):
                    temp_name2 = ""
                    if k!=j:
                        if k == 1:
                            temp_name2 +="a"
                        elif k == 2:
                            temp_name2 +="b"
                        elif k == 3:
                            temp_name2 +="c"
                        elif k == 4:
                            temp_name2 +="d"
                        elif k == 5:
                            temp_name2 +="e"
                        elif k == 6:
                            temp_name2 +="f"
                        elif k == 7:
                            temp_name2 +="g"
                        elif k == 8:
                            temp_name2 +="h"
                        elif k == 9:
                            temp_name2 +="i"
                        temp_name2+= number
                        board_dict[temp_name].add_constraint(temp_name2)



        print(board_dict.keys())
        for key in board_dict:
            if board_dict[key].get_family() == board_dict[temp_name].get_family():
                board_dict[temp_name].add_constraint(board_dict[key].get_name())

                

print("starting")
board = three_board()
print("ending")
from tile import tile
class three_board:
    def __init__(self):
        self.board_dict = {

        }
        self.num_calls = 0
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
                self.board_dict[temp_name] = tile(temp_name)
                if (letter == "a" or letter == "b" or letter == "c") and (number == 1 or number == 2 or number == 3):
                    self.board_dict[temp_name].set_family(1)
                elif (letter == "d" or letter == "e" or letter == "f") and (number == 1 or number == 2 or number == 3):
                    self.board_dict[temp_name].set_family(2)
                elif (letter == "g" or letter == "h" or letter == "i") and (number == 1 or number == 2 or number == 3):
                    self.board_dict[temp_name].set_family(3)
                elif (letter == "a" or letter == "b" or letter == "c") and (number == 4 or number == 5 or number == 6):
                    self.board_dict[temp_name].set_family(4)
                elif (letter == "d" or letter == "e" or letter == "f") and (number == 4 or number == 5 or number == 6):
                    self.board_dict[temp_name].set_family(5)
                elif (letter == "g" or letter == "h" or letter == "i") and (number == 4 or number == 5 or number == 6):
                    self.board_dict[temp_name].set_family(6)
                elif (letter == "a" or letter == "b" or letter == "c") and (number == 7 or number == 8 or number == 9):
                    self.board_dict[temp_name].set_family(7)
                elif (letter == "d" or letter == "e" or letter == "f") and (number == 7 or number == 8 or number == 9):
                    self.board_dict[temp_name].set_family(8)
                elif (letter == "g" or letter == "h" or letter == "i") and (number == 7 or number == 8 or number == 9):
                    self.board_dict[temp_name].set_family(9)
                

                #add column constraints
                for k in range (1,10):
                    temp_add = letter
                    if k!=number:
                        temp_add += str(k)
                        self.board_dict[temp_name].add_constraint(temp_add)
                #add row constraints
                for k in ["a","b","c","d","e","f","g","h","i"]:
                    temp_name2 = k
                    if k != letter:
                        temp_name2+= str(number)
                        self.board_dict[temp_name].add_constraint(temp_name2)
                #fam
        for key in self.board_dict:
            for key2 in self.board_dict:
                if key != key2:
                    if self.board_dict[key].get_family() == self.board_dict[key2].get_family():
                        self.board_dict[key].add_constraint(self.board_dict[key2].get_name())

        
    def print_board(self):
        for i in range(1,10):
            o_str = ""
            for j in ["a","b","c","d","e","f","g","h","i"]:
                key = j + str(i)
                o_str+=str(self.board_dict[key].get_num())
                o_str += " "
            print(o_str)
    def duplicate_board(self):
        new_board = three_board()
        for key in self.board_dict:
            new_board.board_dict[key].set_num(self.board_dict[key].get_num())
            new_board.board_dict[key].set_constraints(self.board_dict[key].get_constraints())
            new_board.board_dict[key].new_domain()
            for i in self.board_dict[key].get_domain():
                new_board.board_dict[key].add_domain(i)
            #new_board.board_dict[key].set_tried(self.board_dict[key].get_tried())
            #new_board.board_dict[key].set_family(self.board_dict[key].get_familt())
        return new_board

    def mod_domains(self,curr_tile,value):
        for constraint in curr_tile.get_constraints():
            self.board_dict[constraint].delete_domain(value)




                

#print("starting")
#board = three_board()
#print("ending")
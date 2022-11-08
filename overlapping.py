from three_board import three_board
from tile import tile
class overlapping:
    def __init__(self):
        self.board_dict = {

        }
        for each_board in range(1,4):
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
                    temp_name+=str(each_board)
                    self.board_dict[temp_name] = tile(temp_name)
                    #print("added ",temp_name, " ",self.board_dict[temp_name].get_name())
                    if (letter == "a" or letter == "b" or letter == "c") and (number == 1 or number == 2 or number == 3):
                        self.board_dict[temp_name].set_family(1+10*each_board)
                    elif (letter == "d" or letter == "e" or letter == "f") and (number == 1 or number == 2 or number == 3):
                        self.board_dict[temp_name].set_family(2+10*each_board)
                    elif (letter == "g" or letter == "h" or letter == "i") and (number == 1 or number == 2 or number == 3):
                        self.board_dict[temp_name].set_family(3+10*each_board)
                    elif (letter == "a" or letter == "b" or letter == "c") and (number == 4 or number == 5 or number == 6):
                        self.board_dict[temp_name].set_family(4+10*each_board)
                    elif (letter == "d" or letter == "e" or letter == "f") and (number == 4 or number == 5 or number == 6):
                        self.board_dict[temp_name].set_family(5+10*each_board)
                    elif (letter == "g" or letter == "h" or letter == "i") and (number == 4 or number == 5 or number == 6):
                        self.board_dict[temp_name].set_family(6+10*each_board)
                    elif (letter == "a" or letter == "b" or letter == "c") and (number == 7 or number == 8 or number == 9):
                        self.board_dict[temp_name].set_family(7+10*each_board)
                    elif (letter == "d" or letter == "e" or letter == "f") and (number == 7 or number == 8 or number == 9):
                        self.board_dict[temp_name].set_family(8+10*each_board)
                    elif (letter == "g" or letter == "h" or letter == "i") and (number == 7 or number == 8 or number == 9):
                        self.board_dict[temp_name].set_family(9+10*each_board)
                    

                    #add column constraints
                    for k in range (1,10):
                        temp_add = letter
                        if k!=number:
                            temp_add += str(k)
                            temp_add+=str(each_board)
                            self.board_dict[temp_name].add_constraint(temp_add)
                    #add row constraints
                    for k in ["a","b","c","d","e","f","g","h","i"]:
                        temp_name2 = k
                        if k != letter:
                            temp_name2+= str(number)
                            temp_name2+= str(each_board)
                            self.board_dict[temp_name].add_constraint(temp_name2)
                    #fam
            for key in self.board_dict:
                for key2 in self.board_dict:
                    if key != key2:
                        if self.board_dict[key].get_family() == self.board_dict[key2].get_family():
                            self.board_dict[key].add_constraint(self.board_dict[key2].get_name())
        #print(self.board_dict.keys())
        b1lets = ["d","e","f","g","h","i"]
        b2lets = ["a","b","c","d","e","f"]
        b1nums = [4,5,6,7,8,9]
        b2nums = [1,2,3,4,5,6]
        for i in range(6):
                for j in range(6):
                    #print("i ", i, " j ",j)
                    name_keep = b1lets[i]+str(b1nums[j])+str(1)
                    name_remove = b2lets[i]+str(b2nums[j])+str(2)
                    tile_keep = self.board_dict[name_keep]
                    tile_remove = self.board_dict[name_remove]
                    self.board_dict.pop(name_keep)
                    self.board_dict.pop(name_remove)
                    self.board_dict[name_keep]=tile_keep.add_tiles(tile_remove)
                    self.replace_constraints(name_keep,name_remove)
        b2lets = ["d","e","f","g","h","i"]
        b3lets = ["a","b","c","d","e","f"]
        b2nums = [4,5,6,7,8,9]
        b3nums = [1,2,3,4,5,6]
        for i in range(6):
                for j in range(6):
                    if(i==0 or i==1 or i==2) and (j==0 or j==1 or j==2):
                        name_keep = b2lets[i]+str(b2nums[j])+str(2)
                        name_remove = b3lets[i]+str(b3nums[j])+str(3)
                        #print(name_keep, " ", name_remove)
                    else:
                        name_keep = b2lets[i]+str(b2nums[j])+str(2)
                        name_remove = b3lets[i]+str(b3nums[j])+str(3)
                        tile_keep = self.board_dict[name_keep]
                        tile_remove = self.board_dict[name_remove]
                        self.board_dict.pop(name_keep)
                        self.board_dict.pop(name_remove)
                        self.board_dict[name_keep]=tile_keep.add_tiles(tile_remove)
                        self.replace_constraints(name_keep,name_remove)
        for key in self.board_dict:
            self.board_dict[key].remove_duplicates()


             

    def replace_constraints(self,name1,name2):
        for key in self.board_dict:
            while name2 in self.board_dict[key].get_constraints():
                if name2 in self.board_dict[key].get_constraints():
                    self.board_dict[key].delete_constraint(name2)
                    self.board_dict[key].add_constraint(name1)
    def print_board(self):
        # for i in range(1,10):
        #     o_str = ""
        #     for j in ["a","b","c","d","e","f","g","h","i"]:
        #         key = j + str(i)
        #         o_str+=str(self.board_dict[key].get_num())
        #         o_str += " "
        #     print(o_str)
        print(self.board_dict)
        print(*self.board_dict.items(), sep='\n')
    def duplicate_board(self):
        new_board = overlapping()
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

























        





        # for i in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]:
        #     for j in range(1,16):
        #         temp_name = i
        #         letter = temp_name
        #         number = j
        #         temp_name += str(j)
        #         self.board_dict[temp_name] = tile(temp_name)
        #         if (letter == "a" or letter == "b" or letter == "c") and (number == 1 or number == 2 or number == 3):
        #             self.board_dict[temp_name].set_family(1)
        #         elif (letter == "d" or letter == "e" or letter == "f") and (number == 1 or number == 2 or number == 3):
        #             self.board_dict[temp_name].set_family(2)
        #         elif (letter == "g" or letter == "h" or letter == "i") and (number == 1 or number == 2 or number == 3):
        #             self.board_dict[temp_name].set_family(3)
        #         elif (letter == "a" or letter == "b" or letter == "c") and (number == 4 or number == 5 or number == 6):
        #             self.board_dict[temp_name].set_family(4)
        #         elif (letter == "d" or letter == "e" or letter == "f") and (number == 4 or number == 5 or number == 6):
        #             self.board_dict[temp_name].set_family(5)
        #         elif (letter == "g" or letter == "h" or letter == "i") and (number == 4 or number == 5 or number == 6):
        #             self.board_dict[temp_name].set_family(6)
        #         elif (letter == "a" or letter == "b" or letter == "c") and (number == 7 or number == 8 or number == 9):
        #             self.board_dict[temp_name].set_family(7)
        #         elif (letter == "d" or letter == "e" or letter == "f") and (number == 7 or number == 8 or number == 9):
        #             self.board_dict[temp_name].set_family(8)
        #         elif (letter == "g" or letter == "h" or letter == "i") and (number == 7 or number == 8 or number == 9):
        #             self.board_dict[temp_name].set_family(9)
        #         elif (letter == "d" or letter == "e" or letter == "f") and (number == 10 or number == 11 or number == 12):
        #             self.board_dict[temp_name].set_family(10)
        #         elif (letter == "j" or letter == "k" or letter == "l") and (number == 4 or number == 5 or number == 6):
        #             self.board_dict[temp_name].set_family(11)
        #         elif (letter == "g" or letter == "h" or letter == "i") and (number == 10 or number == 11 or number == 12):
        #             self.board_dict[temp_name].set_family(12)
        #         elif (letter == "j" or letter == "k" or letter == "l") and (number == 10 or number == 11 or number == 12):
        #             self.board_dict[temp_name].set_family(13)
        #         elif (letter == "m" or letter == "n" or letter == "o") and (number == 10 or number == 11 or number == 12):
        #             self.board_dict[temp_name].set_family(14)
        #         elif (letter == "j" or letter == "j" or letter == "l") and (number == 7 or number == 8 or number == 9):
        #             self.board_dict[temp_name].set_family(15)
        #         elif (letter == "m" or letter == "n" or letter == "o") and (number == 7 or number == 8 or number == 9):
        #             self.board_dict[temp_name].set_family(16)
        #         elif (letter == "g" or letter == "h" or letter == "i") and (number == 13 or number == 14 or number == 15):
        #             self.board_dict[temp_name].set_family(17)
        #         elif (letter == "j" or letter == "k" or letter == "l") and (number == 13 or number == 14 or number == 15):
        #             self.board_dict[temp_name].set_family(18)
        #         elif (letter == "m" or letter == "n" or letter == "o") and (number == 13 or number == 14 or number == 15):
        #             self.board_dict[temp_name].set_family(19)
                
                

        #         #add column constraints
        #         for k in range (1,16):
        #             temp_add = letter
        #             if k!=number:
        #                 temp_add += str(k)
        #                 self.board_dict[temp_name].add_constraint(temp_add)
        #         #add row constraints
        #         for k in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]:
        #             temp_name2 = k
        #             if k != letter:
        #                 temp_name2+= str(number)
        #                 self.board_dict[temp_name].add_constraint(temp_name2)
        #         #fam
        # for key in self.board_dict:
        #     for key2 in self.board_dict:
        #         if key != key2:
        #             if self.board_dict[key].get_family() == self.board_dict[key2].get_family():
        #                 self.board_dict[key].add_constraint(self.board_dict[key2].get_name())

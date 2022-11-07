from three_board import three_board
from tile import tile
class overlapping:
    def __init__(self):
        for i in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]:
            for j in range(1,16):
                temp_name = i
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
                elif (letter == "d" or letter == "e" or letter == "f") and (number == 10 or number == 11 or number == 12):
                    self.board_dict[temp_name].set_family(10)
                elif (letter == "j" or letter == "k" or letter == "l") and (number == 4 or number == 5 or number == 6):
                    self.board_dict[temp_name].set_family(11)
                elif (letter == "g" or letter == "h" or letter == "i") and (number == 10 or number == 11 or number == 12):
                    self.board_dict[temp_name].set_family(12)
                elif (letter == "j" or letter == "k" or letter == "l") and (number == 10 or number == 11 or number == 12):
                    self.board_dict[temp_name].set_family(13)
                elif (letter == "m" or letter == "n" or letter == "o") and (number == 10 or number == 11 or number == 12):
                    self.board_dict[temp_name].set_family(14)
                elif (letter == "j" or letter == "j" or letter == "l") and (number == 7 or number == 8 or number == 9):
                    self.board_dict[temp_name].set_family(15)
                elif (letter == "m" or letter == "n" or letter == "o") and (number == 7 or number == 8 or number == 9):
                    self.board_dict[temp_name].set_family(16)
                elif (letter == "g" or letter == "h" or letter == "i") and (number == 13 or number == 14 or number == 15):
                    self.board_dict[temp_name].set_family(17)
                elif (letter == "j" or letter == "k" or letter == "l") and (number == 13 or number == 14 or number == 15):
                    self.board_dict[temp_name].set_family(18)
                elif (letter == "m" or letter == "n" or letter == "o") and (number == 13 or number == 14 or number == 15):
                    self.board_dict[temp_name].set_family(19)
                
                

                #add column constraints
                for k in range (1,16):
                    temp_add = letter
                    if k!=number:
                        temp_add += str(k)
                        self.board_dict[temp_name].add_constraint(temp_add)
                #add row constraints
                for k in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]:
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


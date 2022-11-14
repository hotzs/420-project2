#add csp solver here
import random
class solver:
    def __init__(self):
        self.number = 0
    def add(self):
        self.number+=1




def solved(dictionary):
    for key in dictionary:
        if dictionary[key].get_num() == 0:
            #print("found a 0")
            return 0
    print("solved")
    return 1

def consistent(dictionary):
    for key in dictionary:
        my_list = dictionary[key].get_constraints()
        for i in my_list:
            if (dictionary[key].get_num() ==  dictionary[i].get_num()) and (key!= i):
                print("found an inconsistentsy ", key, " " ,dictionary[key].get_num(), " ", i, " ",dictionary[i].get_num() )
                return 0
    print("consistent")
    return 1

def select_unassigned_tile(dictionary):
    open_tiles = []
    count = 0
    for key in dictionary:
        if dictionary[key].get_num() == 0:
            open_tiles.append(dictionary[key])
    return (random.choice(open_tiles))
    #return (open_tiles[0])
    
def test_consistent(tile,value,dictionary):
    #print(tile.get_name(), " constraints ", tile.get_constraints() )
    for tiles in tile.get_constraints():
        #if tile.get_name() == "a8":
        #print("tile ", tile.get_name()," value ", value, " tile ",tiles, " tilenum ", dictionary[tiles].get_num() )
        if tiles != tile.get_name():
            if value == dictionary[tiles].get_num():
            #print("found inconsistent: ", value," ", tiles," ", dictionary[tiles].get_num())
                return 0
    return 1



#base

#figure6.5 in textbook
def backtrack(board,level):
    if 0 == 0:
        print("Called backtrack", str(level))
    if solved(board.board_dict) == 1:
        if consistent(board.board_dict) == 1: 
            return board
    curr_tile = select_unassigned_tile(board.board_dict)
    #print("next nodes ",length)
    for value in curr_tile.get_domain():
        if level == 0:
            print("level ",str(level)," trying values", curr_tile .get_name()," ", str(value))
        #if value not in curr_tile.get_tried():
        if test_consistent(curr_tile ,value,board.board_dict) == 1:
                if 0 == 0:
                    print("found consistent at ", curr_tile .get_name()," ", value)
                curr_tile.set_num(value)
                curr_tile.add_tried(value)
                result = backtrack(board.duplicate_board(),level+1)
                if result is not None:
                    if solved(result.board_dict) == 1:
                        if consistent(result.board_dict) == 1: 
                            return result
def CSP_Solver(board,MRV,LCV,FC,AC3,name):
    if AC3:
        AC3_check(board)
    num_calls = 0
    solve = solver()
    return backtrack_MRV_LCV(board,0,MRV,LCV,FC,solve,name)


def backtrack_MRV_LCV(board,level,MRV,LCV,FC,solve,name):
    tracker = ""
    if MRV:
        tracker += "MRV TRUE"
    else:
        tracker += "MRV FALSE"
    if LCV:
        tracker += "LCV TRUE"
    else:
        tracker += "LCV FALSE"
    if FC:
        tracker += "FC TRUE"
    else:
        tracker += "FC FALSE"
  
    solve.add()
    board.num_calls = solve.number
    if 0 == 0:
        print(name," Called backtrack", str(level), " ", tracker)
    if solved(board.board_dict) == 1:
        if consistent(board.board_dict) == 1: 
            return board
    if MRV:
        curr_tile = select_unassigned_mrv(board.board_dict)
    else:
        curr_tile = select_unassigned_tile(board.board_dict)

    #print("next nodes ",length)
    #print(curr_tile.get_name()," domain: ",curr_tile.get_domain())
    #print(curr_tile.get_name(), " constraints ",curr_tile.get_constraints())
    if LCV:
        dom_list = lcv(curr_tile,board.board_dict)
    else:
        dom_list = curr_tile.get_domain()
    if 0 == 73:
        print(curr_tile.get_name()," dom list", dom_list)
        print(curr_tile.get_name()," constraints", curr_tile.get_constraints())
    for value in dom_list:
        if 0 == 73:
            print("level ",str(level)," trying values", curr_tile.get_name()," ", str(value))
            print(curr_tile.get_name()," constraints", curr_tile.get_constraints())
        #if value not in curr_tile.get_tried():
        if test_consistent(curr_tile ,value,board.board_dict) == 1:
                if 0 == 0:
                    print(name," found consistent at ", curr_tile .get_name()," ", value, " ", tracker)
                new_board = board.duplicate_board()
                curr_tile = new_board.board_dict[curr_tile.get_name()]
                if FC:
                    mod_domains(new_board,curr_tile,value)
                curr_tile.set_num(value)
                #curr_tile.add_tried(value)
                # new_board.num_calls = num_calls
                result = backtrack_MRV_LCV(new_board,level+1,MRV,LCV,FC,solve,name)
                if result is not None:
                    if solved(result.board_dict) == 1:
                        if consistent(result.board_dict) == 1: 
                            return result
        

    
#with AC-3
def AC3_check(board):
    for key in board.board_dict:
        if board.board_dict[key].get_num() != 0:
            print("calling mod domains in ac3")
            mod_domains(board,board.board_dict[key],board.board_dict[key].get_num())

#variable/value ordering
def select_unassigned_mrv(dictionary):
    open_tiles = []
    count = 0
    for key in dictionary:
        if dictionary[key].get_num() == 0:
            open_tiles.append(dictionary[key])
    best = 0
    return_tile = open_tiles[0]
    for i in open_tiles:
        count = 0
        for constraint in open_tiles:
            if constraint.get_num() != 0:
                count+=1
        if count > best:
            best = count
            return_tile = constraint
    return return_tile




def lcv(tile, dictionary):
    best = 0
    largest = 0
    ret_list = []
    count_list = []
    domain = []
    for i in tile.get_domain():
        domain.append(i)
    for num in domain:
        count = 0
        for constraint in tile.get_constraints():
            if num in dictionary[constraint].get_domain():
                count +=1
        count_list.append(count)
    #print(domain)
    #print(count_list)
    #THIS FOR LOOP IS NOT FUNCTIONING CORRECTLY
    if len(domain) == 1:
        ret_list.append(domain[0])
        return ret_list
    elif len(domain) == 0:
        return ret_list
    #print(domain)
   # print(count_list)
    while len(domain) !=0:
        largest = 0
        best = 0
        for i in range (len(domain)):
            #rint("count_list ", count_list[i], " best ",best)
            if count_list[i] > best:
                best = count_list[i]
                largest = domain[i]
                #print("largest ",largest)
        #print("largest ",largest, " best ",best)
        #print(domain)
        if largest == 0:
            for i in domain:
                ret_list.append(i)
                domain.remove(i)
            return ret_list
        ret_list.append(largest)
        #print(largest)
        domain.remove(largest)
        count_list.remove(best)
    print(ret_list)
    return ret_list



#with forward checking
def mod_domains(board,curr_tile,value):
        #print(curr_tile.get_constraints())
        for constraint in curr_tile.get_constraints():
            board.board_dict[constraint].delete_domain(value)

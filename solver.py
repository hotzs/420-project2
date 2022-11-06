#add csp solver here
import random
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

def backtrack_MRV_LCV(board,level):
    if 0 == 0:
        print("Called backtrack", str(level))
    if solved(board.board_dict) == 1:
        if consistent(board.board_dict) == 1: 
            return board
    curr_tile = select_unassigned_mrv(board.board_dict)
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
                result = backtrack_MRV_LCV(board.duplicate_board(),level+1)
                if result is not None:
                    if solved(result.board_dict) == 1:
                        if consistent(result.board_dict) == 1: 
                            return result
        

      #inferences = inference(csp, var, value)
    #   if inferences do not fail:
    #     add inferences to assignment
    #     result = backtrack(assignment, csp)
    #     if result is not failure:
    #       return result
    #remove var = value and inferences from assignment

    
#with AC-3

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




def lcv(var, assignment, csp):
    """Least-constraining-values heuristic."""
    return sorted(csp.choices(var),
                  key=lambda val: csp.nconflicts(var, val, assignment))
#with forward checking
def inference(assignment, var_to_update, value, csp):
    """ Assign VALUE to VAR_TO_UPDATE in ASSIGNMENT. Update domains of
       constrained variables from CSP. If any domains are reduced to 1, also
       inference from them. If any domains are reduced to 0, return False.
       Recursive forward checking.
    """
    assignment[var_to_update] = value
    for constraint in csp[var_to_update]:
        if value not in assignment[constraint]:
            continue
        assignment[constraint] = assignment[constraint].replace(value, "")
        remaining = assignment[constraint]
        if len(remaining) == 1:
            if not inference(assignment, constraint, remaining, csp):
                return False
        elif len(remaining) == 0:
            return False
    return True

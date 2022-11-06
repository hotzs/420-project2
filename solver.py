#add csp solver here
import random
def solved(dictionary):
    for key in dictionary:
        if dictionary[key].get_num() == 0:
            return 0
        return 1

def consistent(dictionary):
    for key in dictionary:
        my_list = dictionary[key].get_constraints()
        for i in my_list:
            if dictionary[key].get_num() ==  dictionary[i].get_num():
                return 0
    return 1

def select_unassigned_tile(dictionary):
    open_tiles = []
    count = 0
    for key in dictionary:
        if dictionary[key].get_num() == 0:
            open_tiles.append(dictionary[key])
    return (random.choice(open_tiles))
    
def test_consistent(tile,value,dictionary):
    for tiles in tile.get_constraints():
        if value == dictionary[tiles].num:
            return 0
    return 1



#base

#figure6.5 in textbook
def backtrack(dictionary,level):
    print("Called backtrack", str(level))
    if solved(dictionary) == 1 and consistent(dictionary) == 1: 
        return dictionary
    curr_tile = select_unassigned_tile(dictionary)
    #print("next nodes ",length)
    for value in curr_tile .get_domain():
        print("level ",str(level)," trying values", curr_tile .get_name()," ", str(value))
        if test_consistent(curr_tile ,value,dictionary):
            print("found consistent at ", curr_tile .get_name())
            curr_tile .set_num(value)
            result = backtrack(dictionary,level+1)

      #inferences = inference(csp, var, value)
    #   if inferences do not fail:
    #     add inferences to assignment
    #     result = backtrack(assignment, csp)
    #     if result is not failure:
    #       return result
    #remove var = value and inferences from assignment

    
#with AC-3

#variable/value ordering
def unassigned(assignment, csp):
    bestValue = 10
    bestVar = None
    for var, value in assignment.items():
        if len(value) > 1 and len(value) < bestValue:
            bestValue = len(value)
            bestVar = var
    return bestVar
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

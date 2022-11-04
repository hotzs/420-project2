#add csp solver here

#base

#figure6.5 in textbook
def Backtracking_search(csp):
    return Backtrack(csp,{})

def Backtrack(csp,assignment):
    if assignment:
        return assignment #is complete
    
#with AC-3

#variable/value ordering

#with forward checking
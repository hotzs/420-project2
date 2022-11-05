#add csp solver here
def solved(assignment):
    """ Return TRUE if 1 assignment per tile. """
    return all(len(item) == 1 for item in assignment.values())

def consistent(variable, value, assignment, csp):
    """ Return TRUE if no domain of variables constrained to VARIABLE equals VALUE. """
    return all(assignment[constraint] != value for constraint in csp[variable])

#base

#figure6.5 in textbook
def backtrack(assignment, csp):
  if assignment is complete: return assignment
  var = select-unassigned-variable(csp)
  for each value in order-domain-values(var, assignment, csp):
    if value is consistent with assignment:
      set var = value in assignment
      inferences = inference(csp, var, value)
      if inferences do not fail:
        add inferences to assignment
        result = backtrack(assignment, csp)
        if result is not failure:
          return result
    remove var = value and inferences from assignment
    return failure

    
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

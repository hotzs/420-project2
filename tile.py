from contextlib import nullcontext


class tile:
    def __init__(self, num, name):
        self.num = num
        self.name = name
        self.up_tile = None
        self.down_tile = None
        self.left_tile = None
        self.right_tile = None
        self.contraints = []
        self.domain = [1,2,3,4,5,6,7,8,9]
        self.num = 0
    def constraint_ret():
        #find a way to store a constraint not as a string
        print("Cannot be ")
    def add_constraint(self,name):
        self.constraint.append(name)
from contextlib import nullcontext


class tile:
    def __init__(self, name):
        self.num = 0
        self.name = name
        self.up_tile = None
        self.down_tile = None
        self.left_tile = None
        self.right_tile = None
        self.family = 0
        self.constraints = []
        self.domain = [1,2,3,4,5,6,7,8,9]
        self.tried = []
    def constraint_ret():
        #find a way to store a constraint not as a string
        print("Cannot be ")
    def add_constraint(self,name):
        self.constraints.append(name)
    def add_tried(self,num):
        self.tried.append(num)
    def get_tried(self):
        return self.tried
    def set_tried(self,tried):
        self.tried = tried
    def set_family(self,num):
        self.family = num
    def get_family(self):
        return self.family
    def get_name(self):
        return self.name
    def get_num(self):
        return self.num
    def set_num(self,num):
        self.num = num
    def get_domain(self):
        return self.domain
    def get_constraints(self):
        return self.constraints
    def set_constraints(self,constraints):
        self.constraints = constraints
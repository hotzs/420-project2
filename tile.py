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
    def set_domain(self,domain):
        self.domain = domain
    def delete_domain(self,num):
        if num in self.domain:
            self.domain.remove(num)
    def delete_constraint(self,constraint):
        if constraint in self.constraints:
            self.constraints.remove(constraint)
    def new_domain(self):
        self.domain = []
    def add_domain(self,num):
        self.domain.append(num)
    def get_constraints(self):
        return self.constraints
    def set_constraints(self,constraints):
        self.constraints = constraints
    def add_tiles(self,tile2):
        ret_tile = tile(self.get_name())
        for constraint in self.get_constraints():
            ret_tile.add_constraint(constraint)
        for constraint in tile2.get_constraints():
            if constraint not in ret_tile.get_constraints():
                ret_tile.add_constraint(constraint)
        return ret_tile
    def remove_duplicates(self):
        for i in self.constraints:
            for j in self.constraints:
                if i == j:
                    self.delete_constraint(j)
from contextlib import nullcontext


class tile:
     def __init__(self, num):
        self.num = num
        self.up_tile = None
        self.down_tile = None


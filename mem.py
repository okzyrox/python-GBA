import cpu

class Memory():
    def __init__(self):
        self.mem = []
        self.totalMem = 32000


    
    def addMem(self, param, zone):
        if len(self.mem) == self.mem[zone]:
            return False
        else:
            return self.mem + param
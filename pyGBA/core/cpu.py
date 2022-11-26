from . import *

class String: # Deprecated, delete this soon
    class Instruction:
        # Move
        #def MOV(cond, S):
            #return f"cond = {cond}, S = {S}"

        # Put more here pls

        def ADD(cond = '', S = '', Rd = 0, Rn = 0, Oprnd2 = 0):
            return 'ADD%s%s R%s, R%s, #%s ;' % (cond, S, Rd, Rn, Oprnd2)

    class Execution:
        def parse(instruction):
            list = instruction.split(' ')
            if list[-1] != ';':
                raise SyntaxError()
            return

        def ADD(instruction):
            list = CPU.Execution.parse(instruction)
            return None

class CPU():
    def __init__(self):
        self.registers = [ bytes(4) for n in range(16) ] # An array of 16 registers

        log('Initialized CPU', 0) # Log CPU

    # Utility
    def register_to_int(self, register):
        if isinstance(register, str):
            return self.bytes_to_int(self.registers[int(register[1])])
        return register

    def bytes_to_int(self, bytes):
        return int.from_bytes(bytes, byteorder = 'little')

    def int_to_bytes(self, integer):
        return integer.to_bytes(4, byteorder = 'little')

    ## Logical ALU Operations
    def MOV(self, Rd, Op2, *, cond = None, S = None):
        if isinstance(Op2, str):
            self.registers[Rd] = self.registers[int(Op2[1])]
        else:
            self.registers[Rd] = self.int_to_bytes(Op2)

    def MVN(self, Rd, Op2, *, cond = None, S = None): # Screw Python bitwise NOT
        self.registers[Rd] = self.int_to_bytes(~self.register_to_int(Op2) & 0xFFFFFFFF)

    def ORR(self, Rd, Rn, Op2, *, cond = None, S = None):
        self.registers[Rd] = self.int_to_bytes(self.bytes_to_int(self.registers[Rn]) | self.register_to_int(Op2))

    def EOR(self, Rd, Rn, Op2, *, cond = None, S = None):
        self.registers[Rd] = self.int_to_bytes(self.bytes_to_int(self.registers[Rn]) ^ self.register_to_int(Op2))

    def AND(self, Rd, Rn, Op2, *, cond = None, S = None):
        self.registers[Rd] = self.int_to_bytes(self.bytes_to_int(self.registers[Rn]) & self.register_to_int(Op2))

    def BIC(self, Rd, Rn, Op2, *, cond = None, S = None):
        self.registers[Rd] = self.int_to_bytes(self.bytes_to_int(self.registers[Rn]) & (~self.register_to_int(Op2) & 0xFFFFFFFF))

    def TST(self, Rn, Op2, *, cond = None, P = None):
        pass

    def TEQ(self, Rn, Op2, *, cond = None, P = None):
        pass

    ## Arithmetic ALU Operations

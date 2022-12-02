from . import *

# 'S' == Set Condition Codes
# 'Rn' == 1st Operand Register
# 'Op2' == 2nd Operand Register
# 'Rd' == Destination Register

# reformat to match actual names or??????
# https://iitd-plos.github.io/col718/ref/arm-instructionset.pdf

class String: # Deprecated, delete this soon
    class Instruction:
        # Move
        #def MOV(cond, S):
            #return f"cond = {cond}, S = {S}"

        # Put more here pls

        def ADD(cond = '', SCondCode = '', RegDest = 0, Op1 = 0, Op2 = 0):
            return 'ADD%s%s R%s, R%s, #%s ;' % (cond, SCondCode, RegDest, Op1, Op2)

    class Execution:
        def parse(instruction):
            list = instruction.split(' ')
            if list[-1] != ';':
                raise SyntaxError()
            return

        def ADD(instruction):
            list = CPU.Execution.parse(instruction)
            return None

class Op(): # 'new' replacement for op2 / op1 since they need set conditions codes, move loc if needed
    def __init__(self, count):
        self.set_condition_code = 0 # int_to_bytes needed???, i dont know assembly
        self.op_num = 0 # change to either 1 or 2 on creation

        # self.flag_* = *

        self.opval = None

        self.dest = None

        g = []
    
    def preAddToRegisterArray(self, val):
        self.register_num = CPU.registers[self.dest]
        self.registerval = val

        


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
    

    def addOpReg(self, op:Op): # temp, only for okzyrox testing
        self.registers[op.dest] = self.int_to_bytes(self.bytes_to_int(op.preAddToRegisterArray.registerval))

    ## Logical ALU Operations
    def MOV(self, RegDest, Op2, *, cond = None, SCondCode = None):
        if isinstance(Op2, str):
            self.registers[RegDest] = self.registers[int(Op2[1])]
        else:
            self.registers[RegDest] = self.int_to_bytes(Op2)

    def MVN(self, RegDest, Op2, *, cond = None, SCondCode = None): # Screw Python bitwise NOT
        self.registers[RegDest] = self.int_to_bytes(~self.register_to_int(Op2) & 0xFFFFFFFF)

    def ORR(self, RegDest, Op1, Op2, *, cond = None, SCondCode = None):
        self.registers[RegDest] = self.int_to_bytes(self.bytes_to_int(self.registers[Op1]) | self.register_to_int(Op2))

    def EOR(self, RegDest, Op1, Op2, *, cond = None, SCondCode = None):
        self.registers[RegDest] = self.int_to_bytes(self.bytes_to_int(self.registers[Op1]) ^ self.register_to_int(Op2))

    def AND(self, RegDest, Op1, Op2, *, cond = None, SCondCode = None):
        self.registers[RegDest] = self.int_to_bytes(self.bytes_to_int(self.registers[Op1]) & self.register_to_int(Op2))

    def BIC(self, RegDest, Op1, Op2, *, cond = None, SCondCode = None):
        self.registers[RegDest] = self.int_to_bytes(self.bytes_to_int(self.registers[Op1]) & (~self.register_to_int(Op2) & 0xFFFFFFFF))

    def TST(self, Op1, Op2, *, cond = None, P = None, SCondCode = None):
        # new sys???
        SCondCode = 1
        Op1 = Op(count=1) # temp, waiting approval + read topmost comment & its PDF + 'Op' class
        Op2 = Op(count=2) # temp, waiting approval + read topmost comment & its PDF + 'Op' class

        # will probably move outside of func to remove redefining it every time

        if isinstance(cond, int):
            if cond == None:
                Op1.set_condition_code, Op2.set_condition_code = self.int_to_bytes(1) # set cond code to '1'
            elif cond != None:
                Op1.set_condition_code, Op2.set_condition_code = self.int_to_bytes(cond)
        else:
            return 0
        
        # cant wait for all this code to do absolutely nothing if i went wrong somewhere; more likely since this is stuff
        # that i barely comprehand lol


    def TEQ(self, Op1, Op2, *, cond = None, P = None):
        pass

    ## Arithmetic ALU Operations

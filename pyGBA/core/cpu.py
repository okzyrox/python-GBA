from . import *


# old formatting
# 'S' == Set Condition Codes
# 'Rn' == 1st Operand Register
# 'Op2' == 2nd Operand Register
# 'Rd' == Destination Register

#+++
# 'DoSetCondCode' - checks whether to set a condition code Condition Codes (0, 1)
## 0 - 'Do not set condition codes'
## 1 - 'Set Condition codes'

# 'Op1' - Operand Register 1
# 'Op2' - Operand Register 2
# 'RegDest' - Register Destination

#++

# 'Acc' - Accumulate (0, 1)
## 0 = multiply only
## 1 = multiply and accumulate

# Unknown

# 'P'


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

        self.condition_codes_added = []
        # when adding a condition code, it defines like a 'thing' to tell the CPU about is withou saying specifically
        # for example, 'PL' tells the CPU that the Operand is either 'positive or zero'.
        # FF Link: https://iitd-plos.github.io/col718/ref/arm-instructionset.pdf#%5B%7B%22num%22%3A60%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2Cnull%2C753%2Cnull%5D
    
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
    
    def string_to_bytes(self, string:str):
        return str.encode(string)
        # default is UTF-8 which should be fine bytes-wise
    
    def bytestring_to_string(self, bytestring:bytes):
        return bytestring.decode()
    


    
    def setOpCondCodeCheckThenDo(self, Op:list, CC, DSCC):
        # CC - CondCode
        # DSCC - DoSetCondCode
        if len(Op) != 2 or len(Op) != 1:
            return 0
        else:
            if isinstance(DSCC, int):
                if DSCC != None and CC != None:
                    for i in Op:
                        Op[i].set_condition_code = self.string_to_bytes(CC)
                elif DSCC != None and CC == None:
                    Op[i].set_condition_code = self.string_to_bytes("PL") # ARM Doc - 4.2 - 'The Condition Field'
                    # missing flag support atm so we cant do much with some condition codes
                    ## 'PL' - positive or zero

                    ## check Ln 69
            else:
                return 0


    ## Logical ALU Operations
    def MOV(self, RegDest, Op2, *, CondCode = None, DoSetCondCode = None):
        if isinstance(Op2, str):
            self.registers[RegDest] = self.registers[int(Op2[1])]
        else:
            self.registers[RegDest] = self.int_to_bytes(Op2)

    def MVN(self, RegDest, Op2, *, CondCode = None, DoSetCondCode = None): # Screw Python bitwise NOT
        self.registers[RegDest] = self.int_to_bytes(~self.register_to_int(Op2) & 0xFFFFFFFF)

    def ORR(self, RegDest, Op1, Op2, *, CondCode = None, DoSetCondCode = None):
        self.registers[RegDest] = self.int_to_bytes(self.bytes_to_int(self.registers[Op1]) | self.register_to_int(Op2))

    def EOR(self, RegDest, Op1, Op2, *, CondCode = None, DoSetCondCode = None):
        self.registers[RegDest] = self.int_to_bytes(self.bytes_to_int(self.registers[Op1]) ^ self.register_to_int(Op2))

    def AND(self, RegDest, Op1, Op2, *, CondCode = None, DoSetCondCode = None):
        self.registers[RegDest] = self.int_to_bytes(self.bytes_to_int(self.registers[Op1]) & self.register_to_int(Op2))

    def BIC(self, RegDest, Op1, Op2, *, CondCode = None, DoSetCondCode = None):
        self.registers[RegDest] = self.int_to_bytes(self.bytes_to_int(self.registers[Op1]) & (~self.register_to_int(Op2) & 0xFFFFFFFF))

    def TST(self, Op1, Op2, *, CondCode = None, P = None, DoSetCondCode = None):


        Op1x = Op(count=1) # temp, probably gonna remove soon
        Op2x = Op(count=2) # temp, probably gonna remove soon



        ops = [Op1, Op2]
        try:
            self.setOpCondCodeCheckThenDo(Op=ops, CC=CondCode, DSCC=DoSetCondCode)
        except 0:
            return 0
        
        # cant wait for all this code to do absolutely nothing if i went wrong somewhere; more likely since this is stuff
        # that i barely comprehand lol


    def TEQ(self, Op1, Op2, *, CondCode = None, P = None):
        pass

    ## Arithmetic ALU Operations

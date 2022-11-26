from . import *
import random



class CPU():
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

    def __init__(self):
        self.registers = bytearray(16) # An array of 16 registers

        log('Initialized CPU', 0) # Log CPU

    def execute(self, instruction):
        inst = instruction[:3].upper()
        return getattr(self.Execution, inst)(instruction[3:])

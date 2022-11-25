#from . import *
import cfg
import random

class CPU():
    def __init__(self):
        print("init")
    class inst():
        def MOV(cond, S):
            #return "CPU - MOV executed"
            print(f"cond = {cond}, S = {S}") # debug
            return f"cond = {cond}, S = {S}"
        def MVM(cond, S):
            return {}



def execute(tests_inst = None):
    if tests_inst is None:
        testing = False
        #instruction = emu.getcurrentinstruction # when it is ready
    else:
        p = tests_inst
    
    if len(p) < 1:
        instruction = p[0]
        match instruction:
            case 'MOV':
                if cfg.PRINT_INST == True:
                    print("MOV")
                    print(getattr(CPU.inst, 'MOV')(cond = 2, S = 1))
                else:
                    getattr(CPU.inst, 'MOV')(cond = 2, S = 1)
            case 'MVN':
                return "im tired (MVN)"
    elif len(p) > 1:
        instruction = p
        for i in instruction:
            match i: # temp until better
                case 'MOV':
                    if cfg.PRINT_INST == True:
                        print("MOV")
                        print(getattr(CPU.inst, 'MOV')(cond = 2, S = 1))
                    else:
                        getattr(CPU.inst, 'MOV')(cond = 2, S = 1)
                case 'MVN':
                    return "im tired (MVN)"
        
    

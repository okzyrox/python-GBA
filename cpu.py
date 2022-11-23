import mem, main
import emu
import cfg
import random

class CPU():
    def __init__(self):
        print("init")
    class inst():
        def MOV(cond, S):
            #return "CPU - MOV executed"
            return f"cond = {cond}, S = {S}"



def execute():
    #instruction = emu.getcurrentinstruction # when it is ready
    p = ['MOV', 'NULL']
    instruction = random.choice(p)
    match instruction:
        case 'MOV':
            if cfg.PRINT_INST == True:
                print(getattr(CPU.inst, 'MOV')(cond = 2, S = 1))
            else:
                getattr(CPU.inst, 'MOV')(cond = 2, S = 1)
        case 'MVN':
            return "im tired"

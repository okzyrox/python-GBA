import cpu, mem, cfg

instructions = []

def emu(filepath):
    file = filepath
    while True:
        while len(instructions) >= 0:
            for i in instructions:
                try:
                    getattr(cpu.CPU.inst, f'{i}')
                    res = True
                except:
                    res = False
                if i != None or res == True:
                    return i
        
        # do later when less tired
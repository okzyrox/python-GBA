from . import *

def cpuTest():
    instructions = [
        'ADD R0, R1, #1 ;',
    ]
    cpu = CPU()
    for i in instructions:
        n = cpu.execute(i)
        log(n, 2)
    return cpu

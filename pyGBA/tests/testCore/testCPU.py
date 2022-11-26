from . import *

def cpuTest():
    comm = ['MOV', 'MVN']
    n = cpu.execute(comm)
    print(n)
    return n

from . import *


def cpuTest():
    logger.log('Testing Logical ALU Operations', 0)
    cpu = CPU()
    cpu.MOV(0, 0x01)
    cpu.MVN(1, 'R1')
    cpu.ORR(2, 0, 0x10)
    cpu.EOR(3, 1, 0x01)
    cpu.AND(4, 1, 'R1')
    cpu.BIC(5, 1, 'R2')
    for i in range(16):
        logger.log('Register %s: %s' % (i, hex(cpu.bytes_to_int(cpu.registers[i]))), 0)
    return cpu

from . import *

#### Memory!!! ####
### Memory regions are as follows:
## General Internal Memory
# 00000000-00003FFF   BIOS - System ROM         (16 KBytes)
# 00004000-01FFFFFF   Not used
# 02000000-0203FFFF   WRAM - On-board Work RAM  (256 KBytes) 2 Wait
# 02040000-02FFFFFF   Not used
# 03000000-03007FFF   WRAM - On-chip Work RAM   (32 KBytes)
# 03008000-03FFFFFF   Not used
# 04000000-040003FE   I/O Registers
## Internal Display Memory
# 05000000-050003FF   BG/OBJ Palette RAM        (1 Kbyte)
# 05000400-05FFFFFF   Not used
# 06000000-06017FFF   VRAM - Video RAM          (96 KBytes)
# 06018000-06FFFFFF   Not used
# 07000000-070003FF   OAM - OBJ Attributes      (1 Kbyte)
### Memory information copied from https://problemkaputt.de/gbatek.htm
#### Thank you ####

kb_constant = 1024 # 1024 bytes == 1kb

# Memory size constraints
INTERNAL_MEM = 16 * kb_constant
WRAM_1 = 256 * kb_constant
WRAM_2 = 32 * kb_constant
IO_MEM = 1023
PALETTE_MEM = 1 * kb_constant
VRAM_MEM = 96 * kb_constant
OAM_MEM = 1 * kb_constant

class Memory():
    def __init__(self):
        self.mem = []
        self.totalMem = 32000

    def addMem(self, param, zone):
        if len(self.mem) == self.mem[zone]:
            return False
        else:
            return self.mem + param

class BIOS(Memory):
    def __init__(self):
        super().__init__()

class Work(Memory): # WRAM On-board && WRAM On-chip
    def __init__(self):
        super().__init__()

class VRAM(Memory):
    def __init__(self):
        super().__init__()

class OAM(Memory):
    def __init__(self):
        super().__init__()

class Palette(Memory):
    def __init__(self):
        super().__init__()

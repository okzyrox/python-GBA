from . import *



##!! './mem_inf.md'


kb_constant = 1024 # 1024 bytes == 1kb

# Memory size constraints
BIOS_MEM = 16 * kb_constant
WRAM_1 = 256 * kb_constant
WRAM_2 = 32 * kb_constant
IO_REG = 1023
PALETTE_MEM = 1 * kb_constant
VRAM_MEM = 96 * kb_constant
OAM_MEM = 1 * kb_constant

class Memory():
    def __init__(self, size):
        self.size = size
        self.mem = bytearray(size)

class BIOS(Memory):
    def __init__(self):
        super().__init__(BIOS_MEM)

class Work_OB(Memory): # WRAM On-board
    def __init__(self):
        super().__init__(WRAM_1)

class Work_OC(Memory): # WRAM On-chip
    def __init__(self):
        super().__init__(WRAM_2)

class VRAM(Memory):
    def __init__(self):
        super().__init__(VRAM_MEM)

class OAM(Memory):
    def __init__(self):
        super().__init__(OAM_MEM)

class Palette(Memory):
    def __init__(self):
        super().__init__(PALETTE_MEM)

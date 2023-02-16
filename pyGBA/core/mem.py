from . import *
import random
import inspect

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
BIOS_MEM = 16 * kb_constant
WRAM_1 = 256 * kb_constant
WRAM_2 = 32 * kb_constant
IO_REG = 1023
PALETTE_MEM = 1 * kb_constant
VRAM_MEM = 96 * kb_constant
OAM_MEM = 1 * kb_constant

# Memory exceptions
class MemoryException(Exception):
    def __init__(self, memory_type, message):
        self.memory_type = memory_type
        self.message = str(self.memory_type) + ' failed without a caught exception. Message:\n' + message
        super().__init__(self.message)

class InvalidMemoryLocation(MemoryException):
    def __init__(self, address):
        self.address = address
        super().__init__(inspect.currentframe().f_back.f_locals['self'], 'Memory address %s (%s) is out of bounds' % (self.address, hex(self.address)))

class RAM():
    def __init__(self):
        self.BIOS = BIOS()
        self.WRAM = (Work_OB(), Work_OC())
        self.IO = Memory(IO_REG)
        self.PALETTE = Palette()
        self.VRAM = VRAM()
        self.OAM = OAM()
        logger.log('Allocated RAM', 2) # Log RAM

class Memory():
    def __init__(self, size):
        self.size = size
        self.mem = bytearray(size)

    def check_location(self, address):
        if address < 0 or address > len(self.mem):
            raise InvalidMemoryLocation(address)

    def randomize(self, start, end):
        self.check_location(start); self.check_location(end)
        for n in range(start, end):
            self.mem[n] = random.getrandbits(1)

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

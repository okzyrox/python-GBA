from . import *

def emu():
    logger.log("Initialising Emu Core", 2)
    ram = RAM()
    cpu = CPU()
    logger.log("Successfully started Emu Core", 1)

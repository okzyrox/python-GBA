from . import *

def memTest():
    ram = RAM()
    logger.log('RAM Randomization Test:', 0)
    logger.log('IO Memory hashed before randomization: %s' % hash(str(ram.IO.mem)), 0)
    ram.IO.randomize(0, len(ram.IO.mem))
    logger.log('IO Memory hashed after randomization: %s' % hash(str(ram.IO.mem)), 0)
    return ram

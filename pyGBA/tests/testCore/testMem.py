from . import *

def memTest():
    ram = RAM()
    log('RAM Randomization Test:', 2)
    log('IO Memory hashed before randomization: %s' % hash(str(ram.IO.mem)), 2)
    ram.IO.randomize(0, len(ram.IO.mem))
    log('IO Memory hashed after randomization: %s' % hash(str(ram.IO.mem)), 2)
    return ram

from . import *

log_types = {
    'OK': 0,
    'WARNING': 1,
    'DEBUG': 2,
}

def log(message, type):
    if not type in log_types.values():
        raise IndexError()
    output = '[' + list(log_types)[type] + ']: ' + str(message)
    match type:
        case 0:
            output = '\u001b[32m' + output
        case 1:
            output = '\u001b[33m' + output
        case 2:
            output = '\u001b[35m' + output
        case other:
            pass
    output += '\u001b[0m'
    print(output)

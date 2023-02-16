from . import *
import time


log_levels = [
    'DEBUG', # 0
    'INFO', # 1
    'NOTICE', # 2
    'WARN', # 3
    'ERROR', # 4
    'FATAL' # 5

]

class Logger():
    def __init__(self):
        self.starttime = time.time()
    
    def log(self, message, level):
        lev = ""
        match level:
            case 0 | "DEBUG":
                lev = "DEBUG"
            case 1 | "INFO":
                lev = "INFO"
            case 2 | "NOTICE":
                lev = "NOTICE"
            case 3 | "WARN":
                lev = "WARN"
            case 4 | "ERROR":
                lev = "ERROR"
            case 5 | "FATAL":
                lev = "FATAL"
        
        timenow = time.time() - self.starttime
        timenow = time.strftime("%H:%M:%S", time.gmtime(timenow))
        print("%s |:| %s |:| %s" % (timenow, lev, message))

logger = Logger()
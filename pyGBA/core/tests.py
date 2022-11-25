# from . import cpu ### doesnt work
import cpu


def tests():
    cpuTest()

def cpuTest():
    comm = ['MOV', 'MVN']
    n = cpu.execute(comm)
    print(n)
    return n


if __name__ == "__main__":
    tests()

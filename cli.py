from pyGBA.__main__ import main, test
from os import environ
DEBUG_MODE = environ.get('PYGBA_DEBUG')

if __name__ == '__main__':
    if DEBUG_MODE == '1':
        test() # Run tests
    else:
        main() # Main

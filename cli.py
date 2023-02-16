from pyGBA.__main__ import main, test
from os import environ
#DEBUG_MODE = environ.get('PYGBA_DEBUG') # what
DEBUG_MODE = True

if __name__ == '__main__':
    if DEBUG_MODE:
        test() # Run tests
        main()
    else:
        main() # Main

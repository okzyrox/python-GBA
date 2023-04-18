from GBA.run import main#, test # do later - okzyrox
#from os import environ
#DEBUG_MODE = environ.get('PYGBA_DEBUG') # what
DEBUG_MODE = True

if __name__ == '__main__':
    if DEBUG_MODE:
        #test() # Run tests
        main()
    else:
        main() # Main

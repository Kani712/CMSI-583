import argparse


""" Import from turing_machine.py """
from turing_machine import TuringMachine

parser = argparse.ArgumentParser()

""" Functions rules are read from text files provided """
if __name__ == "__main__":
    parser.add_argument('-f', '--function',
                        dest='function',
                        help='The name of the function, also defines the prefix for all states.',
                        required=True)
    parser.add_argument('-t', '--tape', dest='tape',
                        help='File name of the tape.', required=True)

    options = parser.parse_args()

    tm = TuringMachine(function=options.function)
    tm.describe(f'functions/func_{options.function}.txt')
    tm.read(f'tapes/input_{options.tape}.txt')

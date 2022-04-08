import traceback
import sys

def errorTraceback():
    for line in traceback.format_stack():
        print(line.strip())

def printError(str):
    print('\n' + str + '\n', file=sys.stderr)
    sys.exit(1)
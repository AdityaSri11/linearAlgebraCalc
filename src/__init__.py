import basicFunctions 
import globalFunctions as gf

def mult(a, b):
    if all(isinstance(x, list) for x in a) and all(isinstance(x, list) for x in b):
        return basicFunctions.matrixMultiply(a,b)
    else:
        gf.errorTraceback()
        gf.printError('List of lists not found for matrices A and B')

# Working multiplication
#print(mult([[1,2]], [[3,4], [5,6]]))
# Intential Error:
#print(mult([1,2], [[3,4]]))
import basicOperations 
import globalFunctions as gf

def mult(a, b):
    if all(isinstance(x, list) for x in a) and all(isinstance(x, list) for x in b):
        return basicOperations.matrixMultiply(a,b)
    else:
        gf.errorTraceback()
        gf.printError('List of lists not found for matrices A and B')

# Working multiplication
#print(mult([[1,2]], [[3,4], [5,6]]))
# Intential Error:
#print(mult([1,2], [[3,4]]))

def add(a, b):
    if all(isinstance(x, list) for x in a) and all(isinstance(x, list) for x in b):
        return basicOperations.matrixAdd(a,b)
    else:
        gf.errorTraceback()
        gf.printError('List of lists not found for matrices A and B')

def sub(a, b):
    if all(isinstance(x, list) for x in a) and all(isinstance(x, list) for x in b):
        return basicOperations.matrixSub(a,b)
    else:
        gf.errorTraceback()
        gf.printError('List of lists not found for matrices A and B')

# Working addition
#print(add([[1,2], [7,8]], [[3,4], [5,6]]))
# Intential Error:
print(sub([[1,2] , [1,1]], [[3,4] , [5,6]]))

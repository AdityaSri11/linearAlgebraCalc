import globalFunctions as gf

def matrixMultiply(a, b):

    if len(b) == len(a[0]):

        result = [[0 for x in range(len(b[0]))] for y in range(len(a))]
        
        for i in range(len(a)):
            for j in range(len(b[0])):
                result[i][j] = 0
                for x in range(len(b[0])):           
                    result[i][j] += (a[i][x] * b[x][j])

        return result
    
    else:
        gf.errorTraceback()
        gf.printError('Columns of first matrix must match rows of second matrix!')
        
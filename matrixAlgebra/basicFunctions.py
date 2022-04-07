def matrixMultiply(a, b):

    result = [[0 for x in range(len(b[0]))] for y in range(len(a))]
     
    for i in range(len(a)):
        for j in range(len(b[0])):
            result[i][j] = 0
            for x in range(len(b[0])):           
                result[i][j] += (a[i][x] * b[x][j])

    return result
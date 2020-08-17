def element_wise_multiplication(A, B):
    res = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            res[i][j] = A[i]*B[j]
    return res

def matrix_multiplication(A, B):
    res = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            res[i][j] = 0
            for k in range(len(A[0])):
                res[i][j] += A[i][k] * B[k][j]
    return  res

def column_sum(A):
    res = [[0] for i in len(A)]
    for i in range(len(A)):
        res[i][0] = sum(A[i])
    return res

def matrix_sum(A, B):
    # If you want the sum to be broadcasted in case B is just one column in size, use it as second argument
    res = [[0 for i in range(len(A[0]))] for j in range(len(B))]
    for i in range(len(B)):
        for j in range(len(A[0])):
            try:
                res[i][j] = A[i][j] + B[i][j]
            except:
                res[i][j] = A[i][j] + B[i][0]
    return res

def relu(A):
    res = [[0 for i in range(len(A[0]))] for j in range(len(A))] 
    for i in range(len(A)):
        for j in range(len(A[0])):
            res[i][j] = A[i][j]*(A[i][j]>0)
    return res

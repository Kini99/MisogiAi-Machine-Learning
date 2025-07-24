def addVectors(a,b):
    """Adds two vectors a and b"""
    print("Sum: ",[a[i] + b[i] for i in range(len(a))])

def computeDotProduct(a,b):
    """Computes the dot product of two vectors a and b"""
    print("Dot Product: ",sum(a[i] * b[i] for i in range(len(a))))
    
def checkOrthagonal(a,b):
    """Checks if two vectors a and b are orthogonal"""
    if sum(a[i] * b[i] for i in range(len(a))) == 0:
        print(True)
    else:
        print(False)

a=[1,2,3]
b=[4,5,6]
addVectors(a,b)
computeDotProduct(a,b)
checkOrthagonal(a,b)

def multiplyMatrices(A, B):
    """Multiplies two matrices A and B"""
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    print("Multiplication result: ", result)

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
multiplyMatrices(A, B)
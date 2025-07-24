def dot_product(a, b):
    """
    Calculate the dot product of two vectors.
    """
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    
    print(f"Dot product of {a} and {b} is {result}")


def matrix_multiply(A, B):
    """
    Multiply two matrices A and B.
    """
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")

    result = []
    
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            element = 0
            for k in range(len(A[0])):
                element += A[i][k] * B[k][j]
            row.append(element)
        result.append(row)
    
    print(f"Matrix multiplication result for {A} and {B} is {result}")


def conditional_probability(events):
    """
    Calculate conditional probability P(A|B) = P(A and B) / P(B).
    """

    if events['B'] == 0:
        raise ValueError("P(B) cannot be zero for conditional probability")

    print(f"Conditional probability of events - {events} is {events['A_and_B'] / events['B']}")
    
# Test dot_product
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]
dot_product(vec1, vec2)

# Test matrix_multiply
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
matrix_multiply(A, B)

# Test conditional_probability
events1 = {'A_and_B': 0.12, 'B': 0.4}
conditional_probability(events1)
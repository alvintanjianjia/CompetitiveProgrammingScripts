# Python implementation of the above approach
from typing import List
import numpy as np
 
# Function to multiply two matrices A and B
def multiply(A: List[List[float]], B: List[List[float]],
             N: int) -> List[List[float]]:
    C = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
    return C
 
# Function to calculate the power of a matrix
def matrix_power(M: List[List[float]], p: int, n: int) -> List[List[float]]:
    A = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        A[i][i] = 1
    while (p):
        if (p % 2):
            A = multiply(A, M, n)
        M = multiply(M, M, n)
        p //= 2
    return A
 
# Function to calculate the probability of
# reaching F at time T after starting from S
def findProbability(M: List[List[float]], N: int, F: int, S: int,
                    T: int) -> float:
 
    # Storing M^T in MT
    MT = matrix_power(M, T, N)
 
    # Returning the answer
    return MT[F - 1][S - 1]
 
 
# Driver code
if __name__ == "__main__":
 
    # Adjacency matrix
    # The edges have been stored in the row
    # corresponding to their end-point
    G = [[0, 0.09, 0, 0, 0, 0], [0.23, 0, 0, 0, 0, 0.62],
         [0, 0.06, 0, 0, 0, 0], [0.77, 0, 0.63, 0, 0, 0],
         [0, 0, 0, 0.65, 0, 0.38], [0, 0.85, 0.37, 0.35, 1.0, 0]]

    G = [[0, 0.5, 0, 0, 0, 0.5], [4/9, 0, 0, 3/9, 2/9, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
    G = np.array(G).T
    print(G)
 
    # N is the number of states
    N = 6
    S = 1
    F = 4
    T = 1000
    
    for i in range(0,7):


        print(
            "The probability of reaching {} at time {}\nafter starting from {} is {}\n"
            .format(i, T, S, findProbability(G, N, i, S, T)))

        ans = findProbability(G, N, i, S, T)
        print(ans.as_integer_ratio())

print(0.214285.as_integer_ratio())
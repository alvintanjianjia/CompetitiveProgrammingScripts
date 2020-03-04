from itertools import combinations
import operator as op
from functools import reduce

"""
References:
https://mathworld.wolfram.com/PartitionFunctionP.html
http://mathworld.wolfram.com/PartitionFunctionQ.html
https://en.wikipedia.org/wiki/Triangular_number
"""

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


# Set N here
n = 6

list_triangular = []
for i in range(200):
    list_triangular.append(i*(i+1)/2)
    #print(i*(i+1)/2)

number_of_levels = 0
for element in list_triangular:
    if n > element:
        number_of_levels += 1
    else:
        break


w, h = n, n;
arr = [[0 for x in range(w)] for y in range(h)]
#print(arr)

def fk_this(n,k):
    for i in range(n):
        for j in range(n):
            if i == j:
                arr[i][j] = 1
            elif j == 0:
                arr[i][j] = 0
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-j][j]


fk_this(n,n)

total = 0
for i in range(1,number_of_levels+1):
    x = n-ncr(i,2)
    #print(x)
    total += arr[int(x)][i]
print(total - 1)



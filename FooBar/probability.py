from fractions import Fraction
from fractions import gcd
from copy import deepcopy
import functools

"""
Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

https://math.stackexchange.com/questions/1941244/markov-chain-help
"""



def findterminalidx(m):
        flag = 0
        for i in range(len(m)):
                for j in range(len(m[0])):
                        if m[i][j] != 0:
                                flag = -1
                if flag != -1:
                        flag = i
                        break
                else:
                        flag = 0
        return flag

def computeprobability(m):
        sum = 0
        for i in range(len(m)):
                sum = Fraction(0)
                for j in range(len(m[0])):
                        sum += m[i][j]
                for j in range(len(m[0])):
                                if sum.numerator != 0:
                                        m[i][j] /= sum
        return m

def createidentitymatrix(n):
        m = [[] for i in range(n)]
        for i in range(n):
                m[i] += []
                for j in range(n):
                        m[i] += [Fraction(0)]
                m[i][i] = Fraction(1)
        return m


def IminusQ(I, Q):
        for i in range(len(I)):
                for j in range(len(I[0])):
                        I[i][j] = I[i][j] - Q[i][j]
        return I

def multiplyrow(m, row, k):
    for i in range(len(m[row])):
        m[row][i] *= k
    return m

def addmultipleofrow(m, sourcerow, k, targetrow):
    m1 = multiplyrow(deepcopy(m), sourcerow, k)
    for i in range(len(m[targetrow])):
        if (sourcerow != targetrow):
                m[targetrow][i] += m1[sourcerow][i]
    return m

def invertmatrix(m):
        invertedm =  createidentitymatrix(len(m))
        pass
        for col in range(len(m)):
                diagonalRow = col
                assert(m[diagonalRow][col] != 0)
                k = Fraction(1,m[diagonalRow][col])
                m = multiplyrow(m, diagonalRow, k)
                invertedm = multiplyrow(invertedm, diagonalRow, k)
                sourceRow = diagonalRow
                for targetRow in range(len(m)):
                   if (sourceRow != targetRow):
                        k = -m[targetRow][col]
                        m = addmultipleofrow(m, sourceRow, k, targetRow)
                        invertedm = addmultipleofrow(invertedm, sourceRow,
                                                         k, targetRow)
        return invertedm

def multiplymatrix(m1, m2):
    retVal = []
    rows = len(m1)
    cols = len(m2[0])

    for row in range(rows):
        retVal += [[0]*cols]

    for row in range(rows):
        for col in range(cols):
            num = Fraction(0)
            for i in range(len(m1[0])):
                num += m1[row][i] * m2[i][col]
            retVal[row][col] = num
    return retVal

def lcm(numbers):
        def lcm(a, b):
                return (a * b) / gcd(a, b)
        return functools.reduce(lcm, numbers, 1)

def needswapping(idx1,idx2, m):
        sum1 = sum2 = 0
        for i in range(len(m[0])):
                sum1 += m[idx1][i]
                sum2 += m[idx2][i]
        if sum1 == 0 and sum2 != 0:
                return True
        else:
                return False

def swaprows(idx1, idx2, m):
        for i in range(len(m)):
                temp = m[i][idx2]
                m[i][idx2] = m[i][idx1]
                m[i][idx1] = temp
        temp = m[idx2]
        m[idx2] = m[idx1]
        m[idx1] = temp

def rearrange(m):
        while(True):
                cnt = 0 
                idx1 = 0
                for i in range(len(m)):
                        if needswapping(idx1,i,m):
                                swaprows(idx1,i,m) 
                                cnt += 1
                        idx1 = i
                if cnt == 0:
                        break
        return m

def solution(m):
        m = rearrange(m)
        terminalidx = findterminalidx(m)
        if terminalidx == 0:
                retVal = [0 for x in range(len(m))]
                retVal[0] = 1
                retVal += [1]
                return retVal
        m1 = [[] for x in range(len(m))]
        for i in range(len(m)):
                m1[i] += []
                for j in range(len(m[0])):
                        m1[i] += [Fraction(m[i][j])]
        m1 = computeprobability(m1)
        R = m1[:terminalidx]
        for i in range(len(R)):
                R[i] = R[i][terminalidx:]
        Q = m1[:terminalidx]
        for i in range(len(Q)):
                Q[i] = Q[i][:terminalidx]
        I =  createidentitymatrix(terminalidx)
        I_Q = IminusQ(I, Q)
        I_Q_inverse = invertmatrix(I_Q)
        m = multiplymatrix(I_Q_inverse, R)
        denominators = [x.denominator for x in m[0]]
        numerators = [x.numerator for x in m[0]]
        lcm_denominator =  lcm(denominators)
        retVal = []
        for n, d in zip(numerators, denominators):
                retVal += [n * (lcm_denominator/d)]
        retVal += [lcm_denominator]

        return retVal

#input = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
#print(answer(input))
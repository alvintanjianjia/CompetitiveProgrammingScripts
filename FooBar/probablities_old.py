from math import gcd
a = [1,2,3,4]   #will work for an int array of any length
lcm = 1
for i in a:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)

import numpy as np
#Current state
I = np.matrix([[0.5, 0.5]])
#Transition Matrix
T = np.matrix([[.7, 0.3],
               [.6, 0.4]])
T1 = I * T
# After 1 hours
print (T1)
T2 = T1 * T
# After 2 hours
print (T2)
T3 = T2 * T
# After 3 hours
print (T3)


input = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
initial_state = [0,0.5,0,0,0,0.5]

for i in range(100):
    T = np.array(input)
    initial_state = initial_state @ T

print(initial_state)
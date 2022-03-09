def xor_function(a):
    res = [a,1,a+1,0]
    return res[a%4]

def getxor(a,b):
    return xor_function(b) ^ xor_function(a-1)

def solution(start, length):
    #print(start,'start')
    if length == 1:
        return start
    end = start + pow(length,2) - 1
    #print(end)
    ans = 0
    inter_length = length
    while start < end:
        #print(start, start + inter_length - 1)
        ans = ans ^ getxor(start,start + inter_length - 1)
        start += length
        inter_length -= 1
    return ans


#print(solution(0,3))
#print(solution(17,4))
#print(solution(3,1))

#print(getxor(17,29))
#print(getxor(17,32))
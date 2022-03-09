import math

def parent(x):
    # For most left diagonal / roots
    if math.log(x + 1,2) % 1 == 0:
        return int(2 * x + 1)

    ans = 0
    
    biggest_root = (pow(2,(math.floor(math.log(x + 1,2)))) - 1)

    child = x - biggest_root
    ans += biggest_root
    
    while (math.log(child + 1,2)) % 1 != 0:
        biggest_root = (pow(2,(math.floor(math.log(child+1,2)))) - 1)
        ans += biggest_root
        child = child - biggest_root
        
    parent = pow(2,(math.log(child + 1,2) + 1)) - 1
        
    if x + 1 == parent:
        return int(parent)

    if parent > biggest_root:
        ans = ans - biggest_root
    
    return int(ans + parent)

#for i in range(1,30):
    #print("Parent of " + str(i) + " is " + str(int(parent(i))))

def solution(h,q):
    #a = 15.1 / 10 * 10
    #return [21,a*15,29]
    #(3, [1, 4, 7])
    arr_ans = []
    for element in q:
        if pow(2,h) <= element + 1:
            arr_ans.append(-1)
        else:
            arr_ans.append(parent(element))
    #return [-1]
    return arr_ans

print(solution(5, [19, 14, 28]))
print(solution(3, [7, 3, 5, 1]))
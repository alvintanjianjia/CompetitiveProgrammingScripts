def solution(x,y):
    ans = int((1 + x) * (x/2)) + int((x + x + y - 2) * (y-1)/2)
    return str(ans)





print(solution(3,2))
print(solution(5,10))
print(solution(1,4))


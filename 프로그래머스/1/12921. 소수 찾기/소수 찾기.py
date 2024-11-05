# import math

# def solution(n):
#     answer = 0
#     arr = []
    
#     arr = [True for i in range(n+1)]
    
#     for i in range(2, int(math.sqrt(n))+1):
#         if arr[i] == True:
#             j = 2
            
#             while i * j <= n:
#                 arr[i*j] = False
#                 j += 1
    
#     for i in range(2, n+1):
#         if arr[i] == True:
#             answer += 1
    
#     return answer

import math

def is_prime(a):
    if a == 1:
        return 0
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return 0
    return 1

def solution(n):
    
    cnt = 0
    
    for i in range(2, n+1):
        if is_prime(i):
            cnt += 1

    return cnt
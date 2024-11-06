import math

def solution(n):
        
    if n % int(math.sqrt(n)) == 0:
        return 1
    else:
        return 2
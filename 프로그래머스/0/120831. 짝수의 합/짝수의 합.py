def solution(n):
    array = []
    
    for i in range (2, n+1, 2):
        array.append(i)
            
    return sum(array)


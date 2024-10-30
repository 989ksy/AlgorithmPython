def solution(x):
    num = []
    
    for i in str(x):
        num.append(int(i))
    
    return True if x % sum(num) == 0 else False
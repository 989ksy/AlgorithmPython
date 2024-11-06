def solution(numbers):
    
    checkArr = []
    checkArr = [True for i in range(10)] # 1 ~ 9
    result = 0
    
    for i in numbers:
        if checkArr[i]:
            checkArr[i] = False
        
    for i in range(10):
        if checkArr[i] == True:
            result += i

    return result
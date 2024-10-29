def solution(price, money, count):
    
    charge = 0 # 이용료
    
    for i in range(1, count+1):
        charge += (price * i)
        
    calculate = charge - money # 남는 돈
    
    if calculate > 0:
        return calculate
    else:
        return 0
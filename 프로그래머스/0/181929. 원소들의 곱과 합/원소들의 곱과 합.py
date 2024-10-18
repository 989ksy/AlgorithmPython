def solution(num_list):
    
    a = 1 # 곱
    b = 0 # 합제곱
    
    for i in num_list:
        a *= i
        b += i
        
    return 1 if a < (b*b) else 0
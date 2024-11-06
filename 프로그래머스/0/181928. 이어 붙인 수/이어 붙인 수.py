def solution(num_list):
    
    a = '' # 짝
    b = '' # 홀
    
    for i in (num_list):
        if i % 2 == 0:
            a += str(i)
        else:
            b += str(i)        
                
    return int(a) + int(b)
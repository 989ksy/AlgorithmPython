def solution(s):
    
    p_count = 0
    y_count = 0
    
    for i in s.lower():
        if i == "p":
            p_count += 1
        elif i == "y":
            y_count += 1
    
    return False if p_count != y_count else True
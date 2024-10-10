def solution(my_string):
    m = list(reversed(my_string))
    s = ""
    
    for i in m:
        s += i
    
    return s
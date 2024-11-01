def solution(s):
    
    array = []
    sorted_str = ''
    
    for i in s:
        array.append(i)
    
            
    for x in sorted(array, reverse = True):
        sorted_str += x
        
    return sorted_str
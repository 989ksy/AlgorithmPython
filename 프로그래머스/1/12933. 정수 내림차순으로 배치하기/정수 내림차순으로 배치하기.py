def solution(n):
    
    arr = [ ]
    
    for i in str(n):
        arr.append(i)
        
    arr.sort(reverse = True)
    
    combine_str = ''.join(map(str, arr))
    combine_int = int(combine_str)
     
    return combine_int
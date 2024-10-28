def solution(arr, divisor):
#     answer = [ ]
    
#     for i in arr:
        
#         if i % divisor == 0:
#             answer.append(i)
    
#     if len(answer) == 0:
#         answer.append(-1)
    
#     answer.sort()
    
#     return answer

    array = [i for i in arr if i % divisor == 0]
    array.sort()
    
    return array if len(array) != 0 else [-1]
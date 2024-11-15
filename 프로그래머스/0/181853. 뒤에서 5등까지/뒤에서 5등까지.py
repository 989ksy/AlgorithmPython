def solution(num_list):
    answer = []

    new_list = sorted(num_list)
    
    for i in range(5):
        answer.append(new_list[i])
        
    
    return answer
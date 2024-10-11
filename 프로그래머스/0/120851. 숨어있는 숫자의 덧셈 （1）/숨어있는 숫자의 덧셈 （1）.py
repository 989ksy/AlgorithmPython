def solution(my_string):
    answer = 0
    num_list = [1,2,3,4,5,6,7,8,9]
    
    for i in my_string:
        for num in num_list:
            if i == str(num):
                answer += int(i)
    
    return answer
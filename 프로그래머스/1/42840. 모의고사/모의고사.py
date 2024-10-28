def solution(answers):
    
    answer = [ ]
    
    one = [1,2,3,4,5] # 5
    two = [2,1,2,3,2,4,2,5] # 8
    three = [3,3,1,1,2,2,4,4,5,5] # 10
    
    count = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            count[0] += 1
        if answers[i] == two[i % 8]:
            count[1] += 1
        if answers[i] == three[i % 10]:
            count[2] += 1

    if max(count) == count[0]:
        answer.append(1)
    if max(count) == count[1]:
        answer.append(2)
    if max(count) == count[2]:
        answer.append(3)

    return answer
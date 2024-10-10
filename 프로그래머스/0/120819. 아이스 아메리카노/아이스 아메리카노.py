def solution(money):
    answer = []
    c = 0
    m = 0

    if money - (5500 *(money // 5500)) >= 0:
        
        c = money // 5500
        m = money - (5500 * c)
        
        answer.append(c)
        answer.append(m)
        
        return answer
        
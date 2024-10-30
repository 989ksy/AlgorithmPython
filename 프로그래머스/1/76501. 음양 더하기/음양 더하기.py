def solution(absolutes, signs):
    
    num = [ ]
    
    for i, a in enumerate(signs):
        num.append(-absolutes[i]) if a == False else num.append(absolutes[i])
                    
    return sum(num)
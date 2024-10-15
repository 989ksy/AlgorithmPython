def solution(a, b):
    add = int(str(a)+str(b))
    gop = 2*a*b
    
    if add > gop:
        return add
    elif add < gop:
        return gop
    else :
        return add
    
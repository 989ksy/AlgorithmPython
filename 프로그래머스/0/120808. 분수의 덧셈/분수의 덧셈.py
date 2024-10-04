import math
def solution(numer1, denom1, numer2, denom2):
    top = (numer1 * denom2) + (numer2 * denom1)
    bottom = denom1 * denom2
    
    if math.gcd(top, bottom) == 1:
        return [top, bottom]
    else:
        return [top/ math.gcd(top, bottom), bottom/ math.gcd(top, bottom)]
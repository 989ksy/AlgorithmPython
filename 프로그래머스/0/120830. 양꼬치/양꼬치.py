def solution(n, k):
    # 양꼬치 값
    eat = 12000 * n
    # 내돈내산 음료 값
    drink = 2000 * k
    # 서비스 음료값
    service = 2000 * (n//10)
    
    return eat + drink - service
def solution(numbers):
    
    first = max(numbers) # 배열에서 가장 큰 수
    numbers.remove(max(numbers)) # 가장 큰 수 배열에서 제거
    second = max(numbers) # 두번째로 큰 수
    
    return first * second
    
def solution(s):
    answer = 0
    number_vocab = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i, a in enumerate(number_vocab):
        s = s.replace(a, str(i))
    
    return int(s)
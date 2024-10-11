def solution(my_string, letter):
    # 1. string to list
    new_list = list(my_string)
    
    # 2. Remove item
    while letter in new_list:
        new_list.remove(letter)
        
    # 3. list to String
    return "".join(new_list)
def solution(my_string):
    answer = 0
    my_string = my_string.split()
    for i in range(len(my_string)-1):
        if my_string[i] == '+':
            my_string[i+1] = int(my_string[i-1]) + int(my_string[i+1])
        elif my_string[i] == '-':
            my_string[i+1] = int(my_string[i-1]) - int(my_string[i+1])
    return my_string[-1]
          

def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    answer = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = answer
    return(''.join(my_string))
  
# 방법은 같은데 더 간단한 코드
# 5줄 -> 2줄
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1] , s[num2] = s[num2] , s[num1] 
    return(''.join(s))

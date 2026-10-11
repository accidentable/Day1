# 괄호가 valid 한 지 판단하는 프로그램
# 1. 문자열 중간에서  )가 더 많아진다면 -> 루프에서 잡힘
# 2. 문자열 끝에서 )가 더 많아진다면 -> 마지막 if문에서 잡힘

def is_valid(s):
    answer = True

    open_count = 0
    close_count = 0

    for i in s:
        if close_count > open_count:
            answer = False
        if i == "(":
            open_count += 1
        if i == ")":
            close_count += 1


    if open_count != close_count:
        answer = False

    return answer

print(is_valid("())(())"))

def is_val_stack(s):
    
    st = [] # Stack 선언
    for i in s:
        if i == "(": # 여는 괄호면 stack push
            st.append(i)
        elif i == ")": # 닫는 괄호면 pop : 스택이 비어있으면 error 출력
            if not st:
                return False
            st.pop()
            
    return not st

print(is_val_stack("(()))"))
           
        

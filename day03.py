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

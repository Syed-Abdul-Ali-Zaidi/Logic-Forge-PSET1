def is_valid(expr : str):
    open_count = 0
    for i in expr:
        if i == '(':
            open_count += 1
        elif i == ')':
            if open_count > 0:
                open_count -= 1
            else:
                return False
    return open_count == 0

def fix_broken_exp(expr : str):
    if is_valid(expr):
        return [expr]

    extra_left = 0
    extra_right = 0
    for i in expr:
        if i == '(':
            extra_left += 1
        elif i == ')':
            if extra_left > 0:
                extra_left -= 1
            else:
                extra_right += 1

    result = []
    for i in range(len(expr)):
        if expr[i] == '(' and extra_left > 0:
            exp = expr[:i] + expr[i+1:]
        elif expr[i] == ')' and extra_right > 0:
            exp = expr[:i] + expr[i + 1:]
        else:
            continue

        if is_valid(exp) and exp not in result:
            result.append(exp)
    return result

    
# print('Input:  "()())()"')
# print('Output:',fix_broken_exp("()())()"))
# print()
#
# print('Input:  "(a)())()"')
# print('Output:',fix_broken_exp("(a)())()"))
# print()
#
# print('Input:  ")("')
# print('Output:',fix_broken_exp(")("))
# print()
#
# print('Input:  "abc"')
# print('Output:',fix_broken_exp("abc"))
# print()
#
# print('Input:  "((("')

# print('Output:',fix_broken_exp("((("))

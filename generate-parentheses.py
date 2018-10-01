def generate_parentheses(n):
    def sub_generate_parentheses(paren_set, current_parentheses, left_n, right_n):
        if not left_n and not right_n:
            paren_set.append(current_parentheses)
        if left_n > 0:
            sub_generate_parentheses(paren_set, current_parentheses + '(', left_n - 1, right_n)
        if left_n < right_n:
            sub_generate_parentheses(paren_set, current_parentheses + ')', left_n, right_n - 1)
    
    paren_set = []
    sub_generate_parentheses(paren_set, '', n, n)
    return paren_set

print(generate_parentheses(3))
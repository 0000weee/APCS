def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        # 如果是運算子
        if token == '+' or token == '-' or token == '*' or token == '/':
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left // right   # 整數除法

            stack.append(result)

        # 如果是數字
        else:
            stack.append(int(token))

    return stack[0]

expression = "7 4 -3 * 1 5 + / *"
answer = evaluate_postfix(expression)
print(answer)

def evaluate_addition(expression):
    """計算只有加法的表達式，例如 '1+2+3'"""
    
    parts = expression.split('+')
    total = 0

    for part in parts:
        number = int(part)
        total = total + number

    return total


def evaluate_multiplication(expression):
    """先加後乘，例如 '1+2*3+4'"""

    parts = expression.split('*')
    
    result = 1

    for part in parts:
        value = evaluate_addition(part)
        result = result * value

    return result



def decode_expression(expression):
    """處理逗號分隔的多個表達式，回傳 max - min"""

    parts = expression.split(',')
    values = []

    for part in parts:
        result = evaluate_multiplication(part)
        values.append(result)

    maximum = max(values)
    minimum = min(values)

    return maximum - minimum


def parse_function(codes, index):
    """
    解析 f(...)，回傳：
    - 計算結果
    - 新的 index 位置
    """
    buffer = ''

    while index < len(codes):

        if codes[index] == 'f' and codes[index + 1] == '(':
            index += 2
            value, index = parse_function(codes, index)
            buffer += str(value)

        elif codes[index] == ')':
            index += 1
            return decode_expression(buffer), index

        else:
            buffer += codes[index]
            index += 1


def expand_functions(codes):
    """將所有 f(...) 展開成數字"""
    result = ''
    index = 0

    while index < len(codes):

        if codes[index] == 'f' and codes[index + 1] == '(':
            index += 2
            value, index = parse_function(codes, index)
            result += str(value)
        else:
            result += codes[index]
            index += 1

    return result

# main()

codes = input()
expanded = expand_functions(codes)
answer = evaluate_multiplication(expanded)
print(answer)

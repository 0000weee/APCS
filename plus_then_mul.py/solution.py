def evaluate_addition(expression: str) -> int:
    """計算只有加法的表達式，例如 '1+2+3'"""
    return sum(int(term) for term in expression.split('+'))


def evaluate_multiplication(expression: str) -> int:
    """先加後乘，例如 '1+2*3+4'"""
    result = 1
    for term in expression.split('*'):
        result *= evaluate_addition(term)
    return result


def decode_expression(expression: str) -> int:
    """處理逗號分隔的多個表達式，回傳 max - min"""
    values = [evaluate_multiplication(expr) for expr in expression.split(',')]
    return max(values) - min(values)


def parse_function(codes: str, index: int) -> tuple[int, int]:
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


def expand_functions(codes: str) -> str:
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


def main():
    codes = input()
    expanded = expand_functions(codes)
    answer = evaluate_multiplication(expanded)
    print(answer)


if __name__ == '__main__':
    main()
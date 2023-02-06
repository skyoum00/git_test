def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return "Invalid operator"

print(calculator(1, 2, '+'))
print(calculator(4, 2, '-'))
print(calculator(2, 3, '*'))
print(calculator(8, 4, '/'))


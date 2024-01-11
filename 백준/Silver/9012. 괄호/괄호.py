n = int(input())

for i in range(n):
    line = input()
    stack = []

    for j in line:
        if j == '(':
            stack.append('(')
        elif j == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print('NO')
    else:
        print('YES')
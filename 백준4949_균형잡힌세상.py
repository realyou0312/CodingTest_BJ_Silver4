# 백준 4949번 균형잡힌세상
# https://www.acmicpc.net/problem/4949



import sys
lines = sys.stdin.readlines()

for line in lines[:-1]:
    stack = []
    for t in line:
        if t in '([': # 괄호가 열리는 부분 : stack
            stack.append(t)
        elif t == "]": # 괄호가 하나 닫혔을때 조건 비교
            if not stack or stack.pop() != '[':
                print('no')
                break
        elif t == ')':
            if not stack or stack.pop() != '(':
                print('no')
                break
        elif t == '.': # '.' 인 케이스
            if stack:
                print('no')
            else:
                print("yes")
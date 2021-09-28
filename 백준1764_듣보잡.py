# 백준 1764번 듣보잡
# https://www.acmicpc.net/problem/1764

# 핵심 : sys, 교집합 사용


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = [input().strip() for i in range(n)]
see = [input().strip() for j in range(m)]

intersection = sorted(list(set(listen) & set(see)))

print(len(intersection))

for i in intersection:
    print(i)

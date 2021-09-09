# 백준 1026번 보물
# https://www.acmicpc.net/problem/1026

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0

for i in range(N):
    result += min(A) * max(B) # A의 최소값 B의 최대값의 곱
    A.remove(min(A)) # 사용하고 삭제
    B.remove(max(B))

print(result)
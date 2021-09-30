# 백준 2217번 로프
# https://www.acmicpc.net/problem/2217

n = int(input())

rope = []
weight = []

for i in range(n):
    rope.append(int(input())) # 로프가 버틸 수 있는 무게

rope.sort(reverse=True) # 내림차순 정렬

for i in range(n):
    weight.append(rope[i] * (i+1)) # 로프가 버틸 수 있는 최대 무게 계산

print(max(weight))

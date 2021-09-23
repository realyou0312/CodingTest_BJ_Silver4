#백준 1676번 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676

N = int(input())
res = 1
for i in range(2, N+1):
    res*=i

res = str(res)[::-1] # 문자열 변환

for i in range(len(res)):
    if res[i] != '0':
        print(i)
        break
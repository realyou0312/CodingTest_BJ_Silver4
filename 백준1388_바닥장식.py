# 백준 1338번 바닥장식
# https://www.acmicpc.net/problem/1388

N, M = map(int, input().split())  # 가로세로
li = [input() for _ in range(N)] # 행렬
count = 0

for i in range(N):
    j = 0
    while j < M: # ㅣ 확인절차 - 열체크
        if li[i][j] == '|':
            j += 1
        else:
            count += 1
            while j < M and li[i][j] == '-':
                j += 1
for j in range(M):
    i = 0
    while i < N: # '-' 확인절차 - 행체크
        if li[i][j] == '-':
            i += 1
        else:
            count += 1
            while i < N and li[i][j] == '|':
                i += 1

print(count)
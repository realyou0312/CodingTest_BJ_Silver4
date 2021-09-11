# 백준 1065번 한수
# https://www.acmicpc.net/problem/1065


n = int(input())
answer = 0

for i in range(1, n+1):
    if i <= 99: # 1 ~ 99 는 모두 한수
        answer += 1

    else:
        n_li = list(map(int, str(i))) # 세자리수는 각 자리 분리
        if n_li[0] - n_li[1] == n_li[1] - n_li[2]:
            answer += 1

print(answer)

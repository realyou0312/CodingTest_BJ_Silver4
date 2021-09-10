# 백준 1049번 기타줄
# https://www.acmicpc.net/problem/1049


N, M = list(map(int, input().split()))

m1 = 100000
m2 = 100000

for i in range(M):
    result = list(map(int, input().split()))
    m1 = min(m1, result[0]) # 패키지의 최소값
    m2 = min(m2, result[1]) # 낱개 최소값

if N > 6: # 끊어진 줄의 개수가 6보다 큰 경우
    r = N % 6
    q = N // 6
    # case1 : 최소 금액 패키지를 하나 초과하여 구매 m1*(q+1)
    # case2 : 최소 금액 패키지를 딱 맞게 구매 + 최소 낱개 금액 m1*q + m2*r
    # result = 최소낱개 금액 * N개 m2 * N
    result = [m1 * (q+1), m1*q+m2*r, m2*N]
    if r*m2 > m1: # 나머지와 최소 낱개 곱이 m1보다 큰 경우 가능
        result = min(result[0:2])
    else:
        result = min(result)
else: # 끊어진 줄의 개수가 6 이하인 경우
    result = min(m1, m2*N)

print(result)



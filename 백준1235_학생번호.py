# 백준 1235번 학생번호
# https://www.acmicpc.net/problem/1235


N = int(input())
numbers = [input() for _ in range(N)]

k = 1
while 1:
    if len(set(map(lambda x: x[-k:], numbers))) == N: #슬라이스 주의
        print(k)
        break # 최소값 출력
    k += 1
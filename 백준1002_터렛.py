# 백준 1002번 터렛
# https://www.acmicpc.net/problem/1002


# 원과 원 사이의 관계 이용하기

t = int(input())

# d = 원의 중심 사이의 거리
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5

# 음수 방지
    if r2>r1:
        r1, r2 = r2, r1

    # 조건식 정리
    if d==0:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    else:
        if (r1+r2==d) or (r1-r2==d):
            print(1)
        elif (r1+r2) > d and (r1-r2) < d:
            print(2)
        else:
            print(0)



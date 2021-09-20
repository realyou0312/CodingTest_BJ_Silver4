# 백준 1485번 정사각형
# https://www.acmicpc.net/problem/1485


# 정사각형 조건 따지기 - 서로다른 점 4개 / 대각선 거리가 같다


def check(c):
    side_one = (c[0][0] - c[1][0])**2 + (c[0][1] - c[1][1])**2
    side_two = (c[1][0] - c[3][0])**2 + (c[1][1] - c[3][1])**2
    if side_one != side_two:
        return 0
    side_three = (c[3][0] - c[2][0])**2 + (c[3][1] - c[2][1])**2
    if side_two != side_three:
        return 0
    side_four = (c[2][0] - c[0][0])**2 + (c[2][1] - c[0][1])**2
    if side_three != side_four:
        return 0
    diagonal_one = (c[0][0] - c[3][0]) ** 2 + (c[0][1] - c[3][1])**2
    diagonal_two = (c[2][0] - c[1][0])**2 + (c[2][1] - c[1][1])**2
    if diagonal_one != diagonal_two or side_one + side_two != diagonal_one:
        return 0
    return 1

point = int(input())
for i in range(point):
    coordinates = []
    for j in range(4):
        x, y = list(map(int, input().split()))
        coordinates.append((x, y))
    coordinates.sort(key=lambda a: (a[0], a[1]))
    print(check(coordinates))


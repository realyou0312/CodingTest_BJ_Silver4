# 백준 1063번 킹
# https://www.acmicpc.net/problem/1063

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

move = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB'] # dx, dy와 매치
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

king, stone, N = map(str, input().split())

#움직이는 방향, 알파벳을 리스트에 담아서 index를 통해 매칭시키기
k_point = [alpha.index(king[0]), int(king[1])] # 0~7 1~8
s_point = [alpha.index(stone[0]), int(stone[1])] # 0~7, 1~8

for i in range(int(N)):
    idx = move.index(input())

    # 넘어가는 다음 좌표 nx ny
    nx = k_point[0] + dx[idx]
    ny = k_point[1] + dy[idx]

    if nx < 0 or ny < 1 or nx > 7 or ny > 8: #말판 벗어남
        continue
    if nx == s_point[0] and ny == s_point[1]:
        px = s_point[0] + dx[idx]
        py = s_point[1] + dy[idx]

        if px < 0 or py < 1 or px > 7 or py > 8:
            continue

        # 현재 좌표 갱신
        s_point[0] = px
        s_point[1] = py

    k_point[0] = nx
    k_point[1] = ny

k_result = alpha[k_point[0]] + str(k_point[1])
s_result = alpha[s_point[0]] + str(s_point[1])

print(k_result)
print(s_result)
# 백준 1347 미로만들기
# https://www.acmicpc.net/problem/1347

'''
풀이방법 생각...
1. 리스트에 초기 방향 설정
2. 위치 좌표와 방향 변경하며 이동 좌표 저장
3. 이동하면서 최대, 최소값의 차이고 변의 길이 계산
4. 최종 계산된 크기로 이차원 리스트 생성 -> 미로 완성
5. 미로 출력
'''

com_list = int(input())
commands = input()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dir = 2
pos = [0, 0]
x_list = [0]
y_list = [0]

for command in commands:
    if command == 'L':
        dir = (dir-1) % 4 # 좌측 방향 판단
    elif command == 'R':
        dir = (dir+1) % 4 # 우측 방향 판단
    elif command == 'F':
        x, y = pos
        nx, ny = x + dx[dir], y + dy[dir]
        x_list.append(nx)
        y_list.append(ny)
        pos = [nx, ny]

max_x, min_x, max_y, min_y = max(x_list), min(x_list), max(y_list), min(y_list)
N, M = max_x - min_x + 1, max_y - min_y + 1
start_x, start_y = abs(min_x), abs(min_y)
maze = [['#'] * M for _ in range(N)]
for x, y in zip(x_list, y_list):
    maze[start_x + x][start_y + y] = '.'

for i in maze:
    print(''.join(i))
# 백준 1021번 회전하는 큐
# https://www.acmicpc.net/problem/1021

# 큐

n, m = map(int, input().split()) # [10, 3]

target = list(map(int, input().split()))   # [2, 9, 5]
que = [ _ for _ in range(1, n+1) ] # [1~10]
count = 0

for i in range(m):
    que_len = len(que) # 10
    idx = que.index(target[i]) # 2 = 1 / 9 = 2 / 5 = 3
    # print(idx)

    if idx < que_len - idx:  # 구하고자 하는 위치가 앞쪽인 경우
        while (1):
            if que[0] == target[i]:
                del que[0]
                break
            else:
                que.append(que[0]) # 첫번째 요소 추가, 삭제
                del que[0]
                count += 1  # 이동횟수 증가

    else:
        while (1):
            if que[0] == target[i]:
                del que[0]
                break
            else:
                que.insert(0, que[-1]) # 마지막요소 첫번째로 넣고 삭제
                del que[-1]
                count += 1 # 이동횟수 증가

print(count)
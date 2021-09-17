# 백준 1337번 올바른 배열
# https://www.acmicpc.net/problem/1337

size = int(input()) # 배열의 개수
array = []
max_count = 1

for i in range(size):
    array.append(int(input()))

array.sort() # 배열 입력 받고 정렬

for i in range(size-1): # 그자리 부터 이후 4자리까지의 숫자
    count = 1
    if size-5 > i: # 연결 되어있는 숫자
        for j in range(1, 5):
            if array[i] + 4 >= array[i+j]:
                count += 1
        if count > max_count:
            max_count = count
    else: # 연결 가능한 숫자
        for j in range(1, size-i):
            if array[i] + 4 >= array[i+j]:
                count += 1
        if count > max_count:
            max_count = count
print(5-max_count) # 5-최대값

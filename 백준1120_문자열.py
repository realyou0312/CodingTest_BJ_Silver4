# 백준 1120번 문자열
# https://www.acmicpc.net/problem/1120

# 브루트 포스

A, B = input().split()

N = len(B) - len(A) + 1

count_li = []

for i in range(N): # 길이가 같아질 때 까지
    count = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            count += 1
    count_li.append(count)

print(min(count_li))


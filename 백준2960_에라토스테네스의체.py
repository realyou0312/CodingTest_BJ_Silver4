# 백준 2960 에라토스테네스의 체
# https://www.acmicpc.net/problem/2960


n, k =map(int, input().split())

era = [_ for _ in range(2, n+1)]

nums = []
while era:
    num = era.pop(0)
    nums.append(num)

    tmp = num
    while tmp <= n:
        if tmp in era:
            era.remove(tmp)
            nums.append(tmp)
        tmp += num

print(nums[k-1])


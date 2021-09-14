# 백준 1244번 스위치 켜고 끄기
# https://codinghani.tistory.com/30

# 핵심 : 남자 여자 나누고 /// 스위치 상태 바꾸기

def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return num

N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())

for i in range(students):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for j in range(num, N+1, num):
            change(j)
    # 여자
    else:
        change(num)
        for k in range(N//2):
            if num + k > N or num - k < 1:
                break
            if switch[num+k] == switch[num-k]:
                change(num+k)
                change(num-k)
            else:
                break

for i in range(1, N+1):
    print(switch[i], end=" ")
    if i % 20 == 0: # 20개씩 끊기
        print()

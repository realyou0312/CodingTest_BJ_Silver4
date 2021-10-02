# 백준 2164번
# https://www.acmicpc.net/problem/2164


'''
덱 활용문제
deque : 양쪽 끝에서 삽입, 삭제 모두 가능한 자료구조

deque 메서드
1. append(  )
2. appendleft(  ) 왼쪽끝에 값 추가
3. extend(  ) : 마지막 부분에 병합
4. pop( ) : deque 제일 마지막 부분부터 하나씩 추출 및 삭제
5. popleft( ) : deque 제일 첫 부분부터 추출 및 삭제
6. rotate(count) : 카운트만큼 deque값을 회전

'''


from collections import deque

n = int(input())

deq = deque([i for i in range(1, n + 1)])
while len(deq) > 1:
    deq.popleft()  # 제일 왼쪽값 추출 및 삭제
    deq.append(deq.popleft())  # 맨 끝에 값 추가
print(deq.pop())  # 값 추출 및 삭제

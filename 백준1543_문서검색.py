# 백준 1543번 문서검색
# https://www.acmicpc.net/problem/1543


# 풀이1

doc = input()
word = input()
ans = 0

while True:
    idx = doc.find(word) # 문자열 찾기
    if idx == -1: # 문자열이 없으면 멈춤
        break
    ans += 1
    doc = doc[idx+len(word):] # word 존재하는 경우 word 자르고 재설정

print(ans)

# 풀이2

doc = input()
word = input()
print(doc.count(word))

# 풀이3

doc = input()
word = input()
print(len(doc.split(word)) -1)
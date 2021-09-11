# 백준 1213번 팰린드롬 만들기
# https://www.acmicpc.net/problem/1213

# 팰린드롬 조건 : 짝수개 or 1종류만 홀수개

n = list(map(str, input()))
count_li = [0 for _ in range(26)]
odd = 0

temp = ''
answer = ''

for i in n:
    count_li[ord(i)-65] += 1 # ★n의 알파벳 개수 세서 리스트에 담기

for i in range(26):
    # 홀수인 경우
    if count_li[i] % 2 == 1:
        odd += 1
        temp = chr(i+65)

    answer += chr(i+65) * (count_li[i] // 2)

reverse_answer = list(answer)
reverse_answer.reverse()

if odd > 1:
    print("I'm Sorry Hansoo")
else: # 짝수인 경우 answer + temp(중앙 알파벳) + reverse
    print(answer + temp + ''.join(map(str, reverse_answer)))


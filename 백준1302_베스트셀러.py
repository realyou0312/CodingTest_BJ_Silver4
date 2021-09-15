# 백준 1302번 베스트셀러
# https://idm101.tistory.com/37

# 가장 많이 팔린 책 출력

N = int(input())
books = {}

for i in range(N):
    book = input()
    if book in books:
        books[book] += 1 # 책이 있으면 추가
    else:
        books[book] = 1

answer = max(books.values()) # 책들중 가장 많이 팔린 책
top = []

for book, num in books.items():
    if num == answer:
        top.append(book) # 가장 많이 팔린 책들을 top리스트에 추가

print(sorted(top)[0]) # 최대값 출력
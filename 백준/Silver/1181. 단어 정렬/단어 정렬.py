import sys

n = int(input())

num = [input() for i in range(n)]

num = set(num) #set으로 중복 제거
num = list(num)
num.sort(key=lambda x: (len(x), x)) #lambda를 통해 len(x) 길이로 먼저 정렬 후 x 단어 사전 순으로 정렬

for i in num:
    print(i)
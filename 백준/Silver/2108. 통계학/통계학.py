import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
numlist = []
for i in range(N):
    numlist.append(int(input()))
print(int(round(sum(numlist)/N, 0))) #산술평균
numlist.sort()
print(numlist[N//2]) #중앙값

count = Counter(numlist).most_common()
if len(count) > 1 and count[0][1] == count[1][1]: #최빈값이 2개 이상일 때는 2번째로 작은 값 출력
    print(count[1][0]) #최빈값
else:
    print(count[0][0])
print(max(numlist) - min(numlist)) #범위
import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

A = {}  # 속도는 dictionary!
for i in range(len(cards)):
    A[cards[i]] = 0  # 아무 숫자로 mapping

for j in range(M):
    if checks[j] not in A:
        print(0, end=' ')
    else:
        print(1, end=' ')
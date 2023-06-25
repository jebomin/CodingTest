import sys

n = int(sys.stdin.readline())
num = [0]*10001

for i in range(n):
    a = int(sys.stdin.readline())
    num[a] += 1

for i in range(1, 10001): #오름차순으로 정렬하기 위한 반복문
    if num[i] != 0:
        for j in range(num[i]):
            print(i)
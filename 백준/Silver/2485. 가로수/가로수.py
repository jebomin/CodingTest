import sys
input = sys.stdin.readline
import math

n = int(input())
a = int(input()) # 첫 번째 나무 좌표

A = []

for i in range(n-1):
    num = int(input())
    A.append(num-a) # 나무와 나무 사이 거리
    a = num
    
# A에 들어있는 모든 수들의 최대공약수 찾기
g = A[0] # 첫 번째 나무와 두 번째 나무 사이 거리
for j in range(1,len(A)):
    g = math.gcd(g, A[j])
result = 0
# 둘 사이에 심을 가로수 개수: 간격 // 최대공약수 - 1
for each in A:
    result += each//g -1
print(result)
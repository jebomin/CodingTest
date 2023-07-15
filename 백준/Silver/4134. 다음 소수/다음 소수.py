#n이 0 또는 1일경우, 2 출력후 끝.
#n이 √m 보다 작거나 같은 약수를 가지지 않으면 n 출력후 끝.
#n이 √m 보다 작거나 같은 약수를 가지면 n+=1 후 2번으로 되돌아가기.

import sys
input=sys.stdin.readline
N=int(input())

def check(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

for i in range(N):
    n=int(input())
    while True:
        if n==0 or n==1:
            print(2)
            break
        if check(n):
            print(n)
            break
        else:
            n+=1
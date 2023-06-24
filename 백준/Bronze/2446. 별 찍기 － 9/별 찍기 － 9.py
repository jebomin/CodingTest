n = int(input())
#위쪽 삼각형
for i in range(n, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))
#아래쪽 삼각형, 2부터 시작하는 이유는 마지막 줄을 반복하지 않기 위해서
for j in range(2,n+1,1):
    print(" " * (n-j) + "*" * (2*j-1))
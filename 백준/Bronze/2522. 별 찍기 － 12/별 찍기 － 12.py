n = int(input())

for i in range(1, n+1, 1): #1부터 n까지 범위
    print(" " * (n-i) + "*" * i) #오름차순
for j in range(1, n, 1): #1부터 n-1까지 범위
    print(" " * j + "*" * (n-j)) #내림차순
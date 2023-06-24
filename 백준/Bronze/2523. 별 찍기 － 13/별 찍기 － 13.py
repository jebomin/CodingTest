n = int(input())

for i in range(1, n+1, 1): #1부터 n까지 범위
    print("*"*i)
    
for j in range(n-1, 0, -1): #n-1부터 0까지 범위
    print("*"*j)
#첫번째 줄부터 n-1번째 줄까지 15번처럼 코딩하고 마지막 줄만 별로 쫙 출력하면 되는 문제
n = int(input())

for i in range(1,n,1):
    if i == 1:
        print(' '*(n-i)+'*')
    else:
        print(' '*(n-i)+'*'+' '*(2*i-3)+'*')
        
print('*'*(2*n-1))
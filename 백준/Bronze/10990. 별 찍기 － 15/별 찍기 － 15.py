#해당 코드는 공백은 앞에 있는 공백은 n-i 규칙, 두번째 공백은 2i-3 규칙이라 해당 규칙을 토대로 코딩
n = int(input())

for i in range(1,n+1, 1):
    if i ==1:
        print(' '*(n-i)+'*')
    else:
        print(' '*(n-i)+'*'+' '*(2*i-3)+'*')